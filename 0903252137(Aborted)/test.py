from direct.showbase.ShowBase import *
from panda3d.core import TextureStage

class Test(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.block = self.loader.loadModel("model/block.obj")
        self.block.reparentTo(self.render)
        self.block.setPos(1, 2, 0)
        self.myTexture = self.loader.loadTexture("textures/dirt.png")
        print(TextureStage.getDefault())
        self.block.setTexture(self.myTexture, 4)

app = Test()
app.run()