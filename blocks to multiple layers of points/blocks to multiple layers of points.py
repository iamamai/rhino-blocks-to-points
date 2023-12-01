import rhinoscriptsyntax as rs
import random

def blocks_to_points(layerIndex, blockStart, blockEnd):
    # Get a list of all layer names in the Rhino document
    layers = rs.LayerNames()

    # Get a list of all block names in the Rhino document
    blocks = rs.BlockNames()

    # Get all objects on a specific layer and prompt the user to select points
    points = rs.ObjectsByLayer(layers[layerIndex], select=True)

    for point in points:
        # Generate a random angle within the specified range (0 to 365 degrees) with a step of 90 degrees
        ang = random.randrange(0, 366, 90)

        # Choose a random block from the specified range using random.choice with a slice
        randBlock = random.choice(blocks[blockStart:blockEnd])

        # Insert the randomly chosen block at the selected point with a zero-degree rotation
        rs.InsertBlock(randBlock, point, angle_degrees=0)

# Iterate over layers with indices from 1 to 6 and block indices from 0 to 5
for i in range(1, 7):
    blocks_to_points(i, 0, 5)

# Iterate over layers with indices from 7 to 12 and block indices from 6 to 11
for j in range(7, 13):
    blocks_to_points(j, 6, 12)
