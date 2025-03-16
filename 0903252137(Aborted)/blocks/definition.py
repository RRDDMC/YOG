import asyncio
from random import choice
from ursina import *

blocksDict = {}
blocksList = []


class MetaBlock():
    def __init__(self, id="unknown", name="unknown", texture="model/textures.png", model="model/block.obj", states=None):
        global blocksDict, blocksList
        if states is None:
            states = {}
        if not isinstance(states, dict):
            raise TypeError("states argument must be a dict")
        self.child = []
        self.id = id
        self.name = name
        self.state = "default"
        self.states = states
        self.states["default"] = {"model": model, "texture": texture}
        blocksDict[self.id] = self
        blocksList.append(self)

    def new(self, **kwargs):
        animations = {}
        for key in self.states:
            animations[key] = Entity(**kwargs, **self.states[key])
        rt = Block(meta=self, animations=animations, state="default")
        self.child.append(rt)
        return rt

    async def randomState(self):
        asyncio.create_task(self.changeState(choice(list(self.states.keys()))))

    async def changeState(self, state):
        tasks = []
        self.state = state
        for child in self.child:
            tasks.append(asyncio.create_task(child.changeState(state)))
        for task in tasks:
            await task


class Block(Animator):
    def __init__(self, state="default", meta=None, animations={}):
        Animator.__init__(self, animations=animations)
        self.state = "default"
        self.meta = meta

    async def randomState(self):
        asyncio.create_task(self.changeState(choice(list(self.states.keys()))))

    async def changeState(self, state):
        self.state = state


dirt = MetaBlock("dirt", "Dirt", "textures/dirt.png")
grass = MetaBlock("grass", "Grass", "textures/grassSummer.png", states={"step": {"texture": "textures/grassNormalStep.png"},
                                                                "autumn": {"texture": "textures/grassAutumn.png"},
                                                                "winter": {"texture": "textures/grassWinter.png"},
                                                                "spring": {"texture": "textures/grassSpring.png"}})
water = MetaBlock("water", "Water", "textures/water.gif")
print("Blocks : {}".format(blocksList))
