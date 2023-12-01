import rhinoscriptsyntax as rs
import random

layers = rs.LayerNames()
blocks = rs.BlockNames()
points = rs.GetObjects("Select points")


for point in points:
    ang = random.randrange(0, 366, 45)
    rand = random.randrange(0, len(blocks))
    rs.InsertBlock(blocks[rand], point, angle_degrees = ang) 

print(len(blocks))
print(len(points))
print(rand)

