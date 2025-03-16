from direct.showbase.ShowBase import *
from panda3d.core import TextureStage

class Test(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.block = self.loader.loadModel("model/cube")
        self.block.reparentTo(self.render)
        self.block.setPos(1, 2, 0)
        self.myTexture = self.loader.loadCubeMap('textures/dirt_#.png')
        print(self.myTexture)
        self.block.setTexture(self.myTexture)
        print(dir(self.block))

app = Test()
app.run()