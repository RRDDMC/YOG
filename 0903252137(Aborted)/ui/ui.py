import asyncio
import webbrowser
from ui.debug import updateDebugUI, debugUI
from ursina import *

discordLink = Sprite("textures/discord.png", parent=camera.ui, ppu=10000)
discordLink.collider = 'box'
discordLink.on_click = Func(webbrowser.open, 'https://discord.com/invite/NtaZAfJnsQ')
discordLink.position = Vec3(-0.85, -0.46, 0)
async def updateUI(globals):
    asyncio.create_task(updateDebugUI(globals))
