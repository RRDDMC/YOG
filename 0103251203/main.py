from ursina import *
BLOCK_MODEL_POSITION = Vec3(-0.74, 0.32, 0)
BLOCK_MODEL_SCALE = Vec3(0.3, 0.3, 0.3)

app = Ursina(development_mode=False, use_ingame_console=True)
blocks = ["model/texture.png", "model/textureTemplate.png", "textures/dirt.png", "textures/grassNormalStep.png", "textures/grassNormal.png", "textures/grassWinter.png", "textures/grassSpring.png", "textures/grassSummer.png"]
actualBlock = -1
actualBlockText = Text('')
actualBlockText.position = window.top_left

def relativeBlock(step):
	global blocks, actualBlock, actualBlockText, blockRender
	lastTexture = blockRender.texture
	actualBlock += step
	if actualBlock < 0:
		actualBlock = len(blocks)-1
	elif actualBlock > len(blocks)-1:
		actualBlock = 0
	actualBlockText.text = blocks[actualBlock]
	blockRender.texture = blocks[actualBlock]
	blockModel.texture = blocks[actualBlock]
	if blockRender.texture == lastTexture:
		blockRender.texture = blocks[0]
		blockModel.texture = blocks[0]

blockRender = Entity(model='model/block.obj')
blockModel = Entity(model='quad', parent=camera.ui, position=BLOCK_MODEL_POSITION, scale=BLOCK_MODEL_SCALE)
blockModelDefault = Entity(model='quad', texture='model/textureTemplate.png', parent=camera.ui, position=BLOCK_MODEL_POSITION, scale=BLOCK_MODEL_SCALE)

def input(key):
	global running
	if key in ['left arrow', 'left arrow hold']:
		relativeBlock(-1)
	if key in ['right arrow', 'right arrow hold']:
		relativeBlock(1)
	if key == Keys.escape:
		running = False

window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = True      	# Show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter
EditorCamera()

relativeBlock(1)
running = True
while running:
	app.step()
