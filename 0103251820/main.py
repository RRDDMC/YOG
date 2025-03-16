from blocks.definition import *
from world.generation import *
from render.camera import *
from ursina import *

app = Ursina(development_mode=True, use_ingame_console=True)

def input(key):
	global running, control, rightClick, cameraPivot, rotationNumber
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
	elif key == 'scroll up' and cameraPivot.position * Vec3(0, 1, 0) > Vec3(0, -10, 0):
		cameraPivot.position += rotations[rotationNumber][1]
	elif key == 'scroll down' and cameraPivot.position * Vec3(0, 1, 0) < Vec3(0, 40, 0):
		cameraPivot.position -= rotations[rotationNumber][1]
	elif key == 'r':
		rotationNumber += 1
		if rotationNumber > 3:
			rotationNumber = 0
		world.rotation = rotations[rotationNumber][0]
	
		
def init():
	world = Entity(visible=False)
	return genWorld((75, 75), world, app), world

def update():
	mouse.relative = mouse.lastPosition - mouse.position
	mouse.lastPosition = mouse.position
	if rightClick:
		cameraPivot.position += mouse.relative.x * rotations[rotationNumber][2][0] * 0.87 * (cameraPivot.y + 11)
		cameraPivot.position += mouse.relative.y * rotations[rotationNumber][2][1] * 0.87 * (cameraPivot.y + 11)
	

window.title = 'Your Simmulation Game'		# The window title
window.borderless = False					# Show a border
window.fullscreen = False					# Do not go Fullscreen
window.exit_button.visible = True			# Show the in-game red X that loses the window
window.exit_button.text = "End"
window.fps_counter.enabled = True			# Show the FPS (Frames per second) counter

control = False
rightClick = False
running = True
mouse.lastPosition = Vec3(0, 0, 0)
dat, world = init()
world.visible = True
while running:
	app.step()
