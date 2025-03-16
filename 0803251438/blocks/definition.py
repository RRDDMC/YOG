import asyncio
from random import choice
from ursina import *

blocksDict = {}
blocksList = []


class MetaBlock():
    def __init__(self, id="unknown", name="unknown", texture="model/textures.png", model="model/block.obj", states={}):
        global blocksDict, blocksList
        if not isinstance(states, dict):
            raise TypeError("states argument must be a dict")
        self.child = []
        self.id = id
        self.name = name
        self.states = states
        self.states["default"] = {"model": model, "texture": texture}
        blocksDict[self.id] = self
        blocksList.append(self)

    def new(self, **kwargs):
        rt = Block(states=self.states, **self.states["default"], **kwargs)
        self.child.append(rt)
        return rt

    async def randomState(self):
        asyncio.create_task(self.changeState(choice(list(self.states.keys()))))

    async def changeState(self, state):
        tasks = []
        for child in self.child:
            tasks.append(asyncio.create_task(child.changeState(state)))
        for task in tasks:
            await task


class Block(Entity):
    def __init__(self, states=None, **kwargs):
        Entity.__init__(self, **kwargs)
        if states is None:
            states = {"default": {"textures": "textures/model.png", "model": "model/block.obj"}}
        self.states = states
        self.state = "default"

    async def randomState(self):
        asyncio.create_task(self.changeState(choice(list(self.states.keys()))))

    async def changeState(self, state):
        if state not in self.states.keys():
            raise ValueError("undefined state: '{}'".format(state))
        self.state = state
        for elt in self.states[self.state].keys():
            setattr(self, elt, self.states[self.state][elt])


dirt = MetaBlock("dirt", "Dirt", "textures/dirt.png")
grass = MetaBlock("grass", "Grass", "textures/grassNormal.png", states={"step": {"texture": "textures/grassNormalStep.png"},
                                                                "winter": {"texture": "textures/grassWinter.png"},
                                                                "spring": {"texture": "textures/grassSpring.png"},
                                                                "summer": {"texture": "textures/grassSummer.png"}})
print("Blocks : {}".format(blocksList))
