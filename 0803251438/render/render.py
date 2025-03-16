import asyncio
from asyncio import create_task

from render.camera import *


async def updateRender(globals):
    mouse.relative = mouse.lastPosition - mouse.position
    mouse.lastPosition = mouse.position
    if globals["rightClick"]:
        move = asyncio.create_task(cameraMove())
        await move
    rotation = asyncio.create_task(cameraRotateUpdate())
    await rotation
