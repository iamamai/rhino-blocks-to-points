import rhinoscriptsyntax as rs
import random

# Get a list of all layers in the Rhino document
layers = rs.LayerNames()

# Get a list of all block definitions in the Rhino document
blocks = rs.BlockNames()

# Prompt the user to select points in the Rhino viewport
points = rs.GetObjects("Select points")

# Prompt the user to set the degree interval for rotation
deg = rs.GetInteger("Set degree interval (10, 30, 45, etc)")

# Prompt the user to set the minimum scale factor as a decimal number
scaleMin = rs.GetReal("Set a decimal number (0.5, 1.0, 2.5, etc)")

# Prompt the user to set the maximum scale factor as a larger decimal number
scaleMax = rs.GetReal("Set a larger decimal number")

# Loop through each selected point
for point in points:
    # Generate a random angle within the specified degree interval
    ang = random.randrange(0, 366, deg)

    # Choose a random block from the available block definitions
    rand_block = random.choice(blocks)

    # Generate a random scale factor within the specified range
    randscale = random.uniform(scaleMin, scaleMax)

    # Insert the randomly chosen block at the selected point with random scale and rotation
    rs.InsertBlock(rand_block, point, scale=(randscale, randscale, randscale), angle_degrees=ang)



