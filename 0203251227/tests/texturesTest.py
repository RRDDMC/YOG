from ursina import *

BLOCKS = ["textures/model.png", "model/textureTemplate.png", "textures/dirt.png", "textures/grassNormalStep.png",
          "textures/grassNormal.png", "textures/grassWinter.png", "textures/grassSpring.png",
          "textures/grassSummer.png", "textures/water.gif"]


class TextureTest():
    def __init__(self, blocks):
        global input
        self.app = Ursina(development_mode=True, use_ingame_console=True)

        def input(key):
            print(key)
            if key in ['left arrow', 'left arrow hold']:
                self.relativeBlock(-1)
            if key in ['right arrow', 'right arrow hold']:
                self.relativeBlock(1)
            if key == 'backspace':
                self.running = False
            if key == 'ecape':
                self.running = False

        self.BLOCK_MODEL_POSITION = Vec3(-0.74, 0.32, 0)
        self.BLOCK_MODEL_SCALE = Vec3(0.3, 0.3, 0.3)

        self.blocks = blocks
        self.actualBlock = -1

        self.actualBlockText = Text('')
        self.actualBlockText.position = window.top_left

        self.blockRender = Entity(model='model/block.obj')
        self.blockModel = Entity(model='quad', parent=camera.ui, position=self.BLOCK_MODEL_POSITION,
                                 scale=self.BLOCK_MODEL_SCALE)
        self.blockModelDefault = Entity(model='quad', texture='model/textureTemplate.png', parent=camera.ui,
                                        position=self.BLOCK_MODEL_POSITION, scale=self.BLOCK_MODEL_SCALE)

        window.title = 'Texturing Test Interface'  # The window title
        window.borderless = False  # Show a border
        window.fullscreen = False  # Do not go Fullscreen
        window.exit_button.visible = True  # Show the in-game red X that loses the window
        window.fps_counter.enabled = True  # Show the FPS (Frames per second) counter
        EditorCamera()

        self.running = True
        self.relativeBlock(1)

    def relativeBlock(self, step):
        lastTexture = self.blockRender.texture
        self.actualBlock += step
        if self.actualBlock < 0:
            self.actualBlock = len(self.blocks) - 1
        elif self.actualBlock > len(self.blocks) - 1:
            self.actualBlock = 0
        self.actualBlockText.text = self.blocks[self.actualBlock]
        self.blockRender.texture = self.blocks[self.actualBlock]
        self.blockModel.texture = self.blocks[self.actualBlock]
        if self.blockRender.texture == lastTexture:
            self.blockRender.texture = self.blocks[0]
            self.blockModel.texture = self.blocks[0]

    def run(self):
        while self.running:
            self.app.step()


if __name__ == "__main__":
    import os

    os.chdir("..")
TextureTest(BLOCKS).run()
