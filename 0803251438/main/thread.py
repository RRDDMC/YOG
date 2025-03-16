import asyncio
import threading
import time

from ui.ui import *
from render.render import *
from world.generation import *

async def mainUpdate(vars):
    ui = asyncio.create_task(updateUI(vars))
    render = asyncio.create_task(updateRender(vars))
    generation = updateGeneration(vars)
    await ui
    await render
    await generation

class MainThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.data = {}
        self.running = False
    def run(self):
        global ticks
        self.data["ticks"] = 0
        self.running = True
        while self.running:
            a = time.time()
            asyncio.run(mainUpdate(self.data))
            try:
                time.sleep(0.05 - (time.time() - a))
            except ValueError:
                pass
            self.data["ticks"] += 1
