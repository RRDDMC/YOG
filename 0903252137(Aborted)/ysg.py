"""Main module"""

import sys
import time
import threading

f = open("log.txt", "a")
f.write(time.strftime("%d/%m/%Y %H:%M:%S\n"))
#sys.stdout = f
#sys.stderr = f
from ursina import *

app = Ursina(development_mode=True, use_ingame_console=True)

from main.thread import mainLoop
from ui.debug import *
from world.generation import *

#### Create Dev mode ####

def devMode():
    """Load th dev mode
    Dev mode is used to execute code into the game."""
    inputField = TextField(position=window.bottom_left + Vec2(0, 0.25))  #Create the code inout field
    inputSubmit = Button(parent=inputField, text='Submit', scale=.1,
                         position=Vec2(0.05, 0.05))  #Create the validation button

    def submit(text):
        """Execute like python code arg text content"""
        try:
            exec(text.text)
        except Exception as error:
            print(error)

    inputSubmit.on_click = Func(submit, inputField)  #Bind the three elements


#### Redefine sys.exit to properly close the game ####
sys._exit = sys.exit    #Save sys.exit


def exit(*args):        #Define new exit function
    global running
    running = False


sys.exit = exit         #Bind new exit function


#### Define the key gestion ####


def input(key):
    global running                                                  #Running is used to stop the game
    if key == 'escape up':
        running = False                                             #Stop the game
    elif key == 'control':
        mainLoop.data["control"] = True                             #Save that control is pressed
    elif key == 'control up':
        mainLoop.data["control"] = False                            #Save that control is no longer pressed
    elif key == 'right mouse down':
        mainLoop.data["rightClick"] = True                          #Save that right click is pressed
    elif key == 'right mouse up':
        mainLoop.data["rightClick"] = False                         #Save that right click is no longer pressed
    elif key == 'scroll up':
        asyncio.run(cameraZoomIn(mainLoop.data))                    #Zoom in
    elif key == 'scroll down':
        asyncio.run(cameraZoomOut(mainLoop.data))                   #Zoom out
    elif key == 'right arrow':
        asyncio.run(cameraRotateRight(mainLoop.data))               #Rotate right
    elif key == 'left arrow':
        asyncio.run(cameraRotateLeft(mainLoop.data))                #Rotate left
    elif key == 'f3':
        mainLoop.data["debugUI"] = not mainLoop.data["debugUI"]     #Turn on or off the debug interface
    elif key == 'f1':
        asyncio.run(setCameraToCenter(mainLoop.data))               #Set camera to center


window.title = 'Your Simulation Game'  # The window title
window.borderless = False  # Show a border
window.fullscreen = False  # Do not go Fullscreen
window.exit_button.visible = True  # Show the in-game red X that loses the window
window.exit_button.text = "End"
window.exit_button.on_click = exit
window.fps_counter.enabled = True  # Show the FPS (Frames per second) counter

#devMode(); debugUI = True
mainLoop.data["waterStates"] = [{"model": "model/block.obj", "texture": "textures/water_000.png"},
                            {"model": "model/block.obj", "texture": "textures/water_000.png"}]
mainLoop.data["updateLock"] = threading.RLock()
mainLoop.data["waitingChunk"] = []
mainLoop.data["control"] = False
mainLoop.data["rightClick"] = False
mainLoop.data["debugUI"] = False
mouse.lastPosition = Vec3(0, 0, 0)
mainLoop.data["world"] = Entity(visible=False)
mainLoop.data["worldData"] = {}
for i in mainLoop.data["worldData"].keys():
    print("{}".format(i))
mainLoop.data["world"].visible = True
running = True
mainLoop.start()
checkChunk(mainLoop.data)
while running:
    with mainLoop.data["updateLock"]:
        app.step()
mainLoop.running = False
mainLoop.join()
f.close()
