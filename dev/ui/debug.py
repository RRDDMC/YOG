from render.camera.camera import *

debugUI = False
fps = window.fps_counter
cameraPos = Text('', position=window.top_left)
cameraChunk = Text('', position=window.top_left - Vec2(0, 0.025))
cameraRot = Text('', position=window.top_left - Vec2(0, 0.05))
entity = Text('', position=window.top_left - Vec2(0, 0.075))
ticksText = Text('', position=window.top_left - Vec2(0, 0.1))
cameraPos.color = Color(0., 0., 0., 1.)
cameraChunk.color = Color(0., 0., 0., 1.)
cameraRot.color = Color(0., 0., 0., 1.)
entity.color = Color(0., 0., 0., 1.)

async def updateDebugUI(globals):
    if globals["debugUI"]:
        fps.enabled = True
        cameraPos.text = "Position: {}".format(getCameraPosition())
        cameraChunk.text = "Chunk: {}".format((int((getCameraPosition() * Vec3(1, 0, 0)).x // 8), int((getCameraPosition() * Vec3(0, 0, 1)).z // 8)))
        cameraRot.text = "Rotation: {}".format(camera.rotation)
        ticksText.text = "Ticks: {}".format(globals["ticks"])
        try:
            entityType = "; {}".format(mouse.hovered_entity.meta.id)
        except AttributeError:
            entityType = ""
        try:
            entity.text = "Hovered entity: {}".format(mouse.hovered_entity.parent.position + mouse.hovered_entity.position) + entityType
        except AttributeError:
            try:
                entity.text = "Hovered entity: {}".format(mouse.hovered_entity.position) + entityType
            except AttributeError:
                entity.text = 'None'
    else:
        fps.enabled = False
        cameraPos.text = ''
        cameraChunk.text = ''
        cameraRot.text = ''
        entity.text = ''
        ticksText.text = ''