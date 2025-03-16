import asyncio
from ursina import *

from render.camera.utils import getCameraPosition, rotations, rotationNumber
from world.chunk import Chunk

def checkChunk(data):
    pos = (int((getCameraPosition() * Vec3(1, 0, 0)).x // 8) - 1, int((getCameraPosition() * Vec3(0, 0, 1)).z // 8) - 1, int(round((getCameraPosition() * Vec3(0, 1, 0)).y + 15) / 5))
    newWaitingChunk = []
    for x in range(pos[0] - 1, pos[0] + pos[2] * rotations[rotationNumber][2][0], rotations[rotationNumber][2][0]):
        for y in range(pos[1] - 1, pos[1] + pos[2] * rotations[rotationNumber][2][1], rotations[rotationNumber][2][1]):
            if (x, y) not in data["worldData"].keys():
                newWaitingChunk.append((x, y))
    data["waitingChunk"] = newWaitingChunk.copy()
async def updateGeneration(data):
    tasks = []
    try:
        x, y = data["waitingChunk"].pop(0)
        data["worldData"][(x, y)] = Chunk(data["world"], position=Vec3(x, 0, y))
        tasks.append(asyncio.create_task(data["worldData"][(x, y)].generate()))
    except IndexError:
        pass
    for task in tasks:
        await task