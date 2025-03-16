"""Main module"""

import asyncio
import sys
import time
f = open("log.txt", "a")
f.write(time.strftime("%d/%m/%Y %H:%M:%S\n"))
#sys.stdout = f
#sys.stderr = f
from ursina import *

app = Ursina(development_mode=True, use_ingame_console=True)

from main.thread import *
from ui.debug import *
from world.generation import *

def devMode():
    inputField = TextField(position=window.bottom_left + Vec2(0, 0.25))
    inputSubmit = Button(parent=inputField, text='Submit', scale=.1, position=Vec2(0.05, 0.05))
    def submit(text):
        try:
            exec(text.text)
        except Exception as error:
            print(error)
    inputSubmit.on_click = Func(submit, inputField)

sys._exit = sys.exit
def exit(*args):
    global running
    running = False
sys.exit = exit

def input(key):
    global running, main
    if key == 'escape up':
        running = False
    elif key == 'control':
        main.data["control"] = True
    elif key == 'control up':
        main.data["control"] = False
    elif key == 'right mouse down':
        main.data["rightClick"] = True
    elif key == 'right mouse up':
        main.data["rightClick"] = False
    elif key == 'scroll up':
        asyncio.run(cameraZoomIn(main.data))
    elif key == 'scroll down':
        asyncio.run(cameraZoomOut(main.data))
    elif key == 'right arrow':
        asyncio.run(cameraRotateRight(main.data))
    elif key == 'left arrow':
        asyncio.run(cameraRotateLeft(main.data))
    elif key == 'f3':
        main.data["debugUI"] = not main.data["debugUI"]
    elif key == 'f1':
        asyncio.run(setCameraToCenter(main.data))

window.title = 'Your Simulation Game'  # The window title
window.borderless = False  # Show a border
window.fullscreen = False  # Do not go Fullscreen
window.exit_button.visible = True  # Show the in-game red X that loses the window
window.exit_button.text = "End"
window.exit_button.on_click = exit
window.fps_counter.enabled = True  # Show the FPS (Frames per second) counter

main = MainThread()
#devMode(); debugUI = True
main.data["waitingChunk"] = []
main.data["control"] = False
main.data["rightClick"] = False
main.data["debugUI"] = False
mouse.lastPosition = Vec3(0, 0, 0)
main.data["world"] = Entity(visible=False)
main.data["worldData"] = {}
for i in main.data["worldData"].keys():
    print("{}".format(i))
main.data["world"].visible = True
running = True
main.start()
checkChunk(main.data)
while running:
    app.step()
main.running = False
main.join()
f.close()