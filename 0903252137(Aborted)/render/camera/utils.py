from ursina import *

cameraPivot = Entity(rotation=Vec3(0, 0, 0), position=Vec3(-11.5, -30, 8.5))
camera.parent = cameraPivot
camera.rotation = Vec3(45, 45, 0)
rotations = [ \
    (Vec3(1, -1, 1), (Vec3(1, 0, -1), Vec3(1, 0, 1)), (1, 1)),
    (Vec3(1, -1, -1), (Vec3(-1, 0, -1), Vec3(1, 0, -1)), (1, -1)),
    (Vec3(-1, -1, -1), (Vec3(-1, 0, 1), Vec3(-1, 0, -1)), (-1, -1)),
    (Vec3(-1, -1, 1), (Vec3(1, 0, 1), Vec3(-1, 0, 1)), (-1, 1))]
rotationNumber = 0
goalRotation = Vec3(45, 45, 0)
worldLimit = 8 ** 2

def getCameraPosition():
    return Vec3(cameraPivot.position - Vec3(-11.5, -30, 8.5))