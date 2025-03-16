import asyncio
from ursina import *

from render.camera import getCameraPosition, rotations, rotationNumber
from world.chunk import Chunk

async def updateGeneration(globals):
    pos = (int((getCameraPosition() * Vec3(1, 0, 0)).x // 8) - 1, int((getCameraPosition() * Vec3(0, 0, 1)).z // 8) - 1, int(round((getCameraPosition() * Vec3(0, 1, 0)).y + 20) / 4))
    tasks = []
    for x in range(pos[0] - 1, pos[0] + pos[2] * rotations[rotationNumber][2][0], rotations[rotationNumber][2][0]):
        for y in range(pos[1] - 1, pos[1] + pos[2] * rotations[rotationNumber][2][1], rotations[rotationNumber][2][1]):
            try:
                if not globals["worldData"][(x, y)].generated and len(tasks) < 2:
                    tasks.append(asyncio.create_task(globals["worldData"][(x, y)].generate()))
            except KeyError:
                globals["worldData"][(x, y)] = Chunk(globals["world"], position=Vec3(x, 0, y))
                if len(tasks) < 2:
                    tasks.append(asyncio.create_task(globals["worldData"][(x, y)].generate()))
    for task in tasks:
        await task