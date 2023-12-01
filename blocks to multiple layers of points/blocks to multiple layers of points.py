import rhinoscriptsyntax as rs
import random

def blocks_to_points(layerIndex, blockStart, blockEnd):
    layers = rs.LayerNames()
    blocks = rs.BlockNames()
    points = rs.ObjectsByLayer(layers[layerIndex], select=True)

    for point in points:
        ang = random.randrange(0, 366, 90)
        randBlock = random.randrange(blockStart, blockEnd)
        rs.InsertBlock(blocks[randBlock], point, angle_degrees = 0)

for i in range(1, 7):
    blocks_to_points(i, 0, 5)

for j in range(7, 13):
    blocks_to_points(j, 6, 12)



