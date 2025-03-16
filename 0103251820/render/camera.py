from ursina import *

cameraPivot = Entity(rotation=Vec3(45, 45, 0), position=Vec3(0, 0, 0))
camera.parent = cameraPivot
#Rotations indices.
#Firt indice 	> Camera rotation.
#Second indice	> Zoom parameters
#Third indice	> Camera position
rotations =  [\
(Vec3(0, 0, 0), Vec3(1, -1, 1), (Vec3(1,0,-1), Vec3(1,0,1))),
(Vec3(0, 90, 0), Vec3(1, -1, -1), (Vec3(-1,0,-1), Vec3(1,0,-1))),
(Vec3(0, 180, 0), Vec3(-1, -1, -1), (Vec3(-1,0,1), Vec3(-1,0,-1))),
(Vec3(0, 270, 0), Vec3(-1, -1, 1)), (Vec3(1,0,1), Vec3(-1,0,1))]
rotationNumber = 0
