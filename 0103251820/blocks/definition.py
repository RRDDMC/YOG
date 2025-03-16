from ursina import *

blocksDict = {}
blocksList = []

class MetaBlock():
	def __init__(self, id="unknown", name="unknown", texture="model/textures.png", model="model/block.obj", states={}):
		global blocksDict, blocksList
		if not isinstance(states, dict):
			raise TypeError("states argument must be a dict")
		self.childs = []
		self.id = id
		self.name = name
		self.states = states
		self.states["default"] = {"model":model, "texture":texture}
		blocksDict[self.id] = self
		blocksList.append(self)
	def new(self, **kwargs):
		rt = Block(states=self.states,**self.states["default"], **kwargs)
		self.childs.append(rt)
		return rt
	def randomState(self):
		self.changeState(choice(list(self.states.keys())))
	def changeState(self, state):
		for child in self.childs:
			child.changeState(state)
class Block(Entity):
	def __init__(self, states={"default":{"texture":"model/texture.png", "model":"model/block.obj"}}, **kwargs):
		Entity.__init__(self, **kwargs)
		self.states = states
		self.state = "default"
	def randomState(self):
		self.changeState(choice(list(self.states.keys())))
	def changeState(self, state):
		if state not in self.states.keys():
			raise ValueError("undefined state: '{}'".format(state))
		self.state = state
		for elt in self.states[self.state].keys():
			setattr(self, elt, self.states[self.state][elt])

MetaBlock("dirt", "Dirt", "textures/dirt.png")
MetaBlock("grass", "Grass", "textures/grassNormal.png", states={"step":{"texture":"textures/grassNormalStep.png"}, "winter":{"texture":"textures/grassWinter.png"}, "spring":{"texture":"textures/grassSpring.png"}, "summer":{"texture":"textures/grassSummer.png"}})
