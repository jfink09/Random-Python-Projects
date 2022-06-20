# Import necessary libraries
import random

# Create an list of each type of orientation that can be made on a Rubik's Cube
orientations = ["F","R","U","L","B","D","F'","R'","U'","L'","B'","D'","2F","2R","2U","2L","2B","2D"]

# Create a duplicate list of orientations to double the length of the scrambling algorithm
extended_orientations = ["F","R","U","L","B","D","F'","R'","U'","L'","B'","D'","2F","2R","2U","2L","2B","2D"]

# Extend the length of the orientation list by using extend()
orientations.extend(extended_orientations)

# Apply randomization the the updated orientation list to ge the scrambling algorithm
random.shuffle(orientations)

# Print the scrambling algorithm
print(*orientations)