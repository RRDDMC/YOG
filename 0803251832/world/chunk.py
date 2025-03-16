import asyncio
from ursina import *
from random import choice
from blocks.definition import blocksList


class Chunk(Entity):
    def __init__(self, world, position=Vec3(0, 0, 0), *args, **kwargs):
        Entity.__init__(self, position=position * Vec3(8, 0, 8) + Vec3(0, -45, 0), parent=world, *args, **kwargs)

        self.visible = False
        self.data = None
    def get_generated(self):
        return bool(self.data)

    generated = property(get_generated)

    async def generate(self):
        pos = Vec3(0, 0, 0)
        self.data = []
        for _ in range(8):
            elt = []
            for _ in range(8):
                elt.append(choice(blocksList).new(position=pos, parent=self, collider='box'))
                pos += Vec3(1, 0, 0)
            self.data.append(elt)
            pos += Vec3(-len(elt), 0, 1)
        self.visible = True
