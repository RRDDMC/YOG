from random import choice
from ursina import *
from blocks.definition import blocksList


def genWorld(size, world, app):
    text = Text(position=window.top)
    pos = Vec3(-size[0] // 2, 0, -size[1] // 2)
    rt = []
    number = 0
    tot = size[0] * size[1]
    text.text = "{}/{} blocks generated".format(number, tot)
    app.step()
    for _ in range(size[1]):
        elt = []
        for _ in range(size[0]):
            elt.append(choice(blocksList).new(position=pos, parent=world))
            elt[-1].randomState()
            pos += Vec3(1, 0, 0)
            number += 1
        text.text = "{}/{} blocks generated".format(number, tot)
        app.step()
        rt.append(elt)
        pos += Vec3(-len(elt), 0, 1)
    text.text = "Generated !"
    return rt
