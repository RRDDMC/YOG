from render.camera.camera import *


async def updateRender(data):
    mouse.relative = mouse.lastPosition - mouse.position
    mouse.lastPosition = mouse.position
    if data["rightClick"]:
        move = asyncio.create_task(cameraMove(data))
        await move
        checkChunk(data)
    rotation = asyncio.create_task(cameraRotateUpdate())
    await rotation
