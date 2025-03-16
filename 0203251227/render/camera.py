from ursina import *

cameraPivot = Entity(rotation=Vec3(45, 45, 0), position=Vec3(0, 0, 0))
camera.parent = cameraPivot
# Rotations indices.
# Firt indices 	> Camera rotation.
# Second indices	> Zoom movement
# Third indices	> Camera position
rotations = [ \
    (Vec3(45, 45, 0), Vec3(1, -1, 1), (Vec3(1, 0, -1), Vec3(1, 0, 1))),
    (Vec3(45, 135, 0), Vec3(1, -1, -1), (Vec3(-1, 0, -1), Vec3(1, 0, -1))),
    (Vec3(45, 225, 0), Vec3(-1, -1, -1), (Vec3(-1, 0, 1), Vec3(-1, 0, -1))),
    (Vec3(45, 315, 0), Vec3(-1, -1, 1), (Vec3(1, 0, 1), Vec3(-1, 0, 1)))]
rotationNumber = 0
goalRotation = Vec3(45, 45, 0)


def cameraMove():
    cameraPivot.position += mouse.relative.x * rotations[rotationNumber % 4][2][0] * 0.87 * (cameraPivot.y + 11)
    cameraPivot.position += mouse.relative.y * rotations[rotationNumber % 4][2][1] * 0.87 * (cameraPivot.y + 11)


def cameraZoomIn():
    if cameraPivot.position * Vec3(0, 1, 0) > Vec3(0, -10, 0):
        cameraPivot.position += rotations[rotationNumber % 4][1]


def cameraZoomOut():
    if cameraPivot.position * Vec3(0, 1, 0) < Vec3(0, 25, 0):
        cameraPivot.position -= rotations[rotationNumber % 4][1]


def cameraRotate():
    global rotationNumber, goalRotation
    rotationNumber += 1
    if rotationNumber > 3:
        rotationNumber = rotationNumber % 4
    goalRotation = rotations[rotationNumber % 4][0]


def cameraRotateUpdate():
    global goalRotation
    if cameraPivot.rotation != goalRotation:
        cameraPivot.rotation += Vec3(0, 5, 0)
        if cameraPivot.rotation * Vec3(0, 1, 0) == Vec3(0, 360, 0):
            cameraPivot.rotation = cameraPivot.rotation * Vec3(1, 0, 1)
