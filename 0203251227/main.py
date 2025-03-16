from blocks.definition import *
from world.generation import *
from render.camera import *
from ursina import *

app = Ursina(development_mode=True, use_ingame_console=True)


def input(key):
    global running, control, rightClick, cameraPivot
    print(key)
    if key == 'escape up':
        running = False
    elif key == 'control':
        control = True
    elif key == 'control up':
        control = False
    elif key == 'right mouse down':
        rightClick = True
    elif key == 'right mouse up':
        rightClick = False
    elif key == 'scroll up':
        cameraZoomIn()
    elif key == 'scroll down':
        cameraZoomOut()
    elif key == 'r':
        cameraRotate()


def init():
    world = Entity(visible=False)
    return genWorld((75, 75), world, app), world


def update():
    mouse.relative = mouse.lastPosition - mouse.position
    mouse.lastPosition = mouse.position
    if rightClick:
        cameraMove()
    if running:
        cameraRotateUpdate()


window.title = 'Your Simulation Game'  # The window title
window.borderless = False  # Show a border
window.fullscreen = False  # Do not go Fullscreen
window.exit_button.visible = True  # Show the in-game red X that loses the window
window.exit_button.text = "End"
window.fps_counter.enabled = True  # Show the FPS (Frames per second) counter

control = False
rightClick = False
running = False
mouse.lastPosition = Vec3(0, 0, 0)
dat, world = init()
world.visible = True
running = True
while running:
    app.step()
