"""
Advent of Code 2025
https://adventofcode.com/2025/day/9
Gemma McLean
"""

# ------
# Read Input
# ------

# List for positions of red tiles
positions = []
# Read in the input file and store each position in list
with open('day09/input.txt') as file_object:
    # Get position as a list of ints [x,y]
    for line in file_object:
        positions.append([int(coord) for coord in line.strip().split(',')])

# ------
# Part 1
# ------

# Track the largest rectangle area found
largest_area_size = 0

# Loop through each unique pair of red tiles
for i in range(len(positions)):
    for j in range(i, len(positions)):
        # Check if the corners can make a rectangle (x and y not the same)
        if positions[i][0] != positions[j][0] and positions[i][1] != positions[j][1]:
            # Calculate the area of the rectange made by the two corners
            x_size = abs(positions[i][0] - positions[j][0]) + 1
            y_size = abs(positions[i][1] - positions[j][1]) + 1
            area_size = x_size * y_size
            # Update largest area size if this one is bigger
            if area_size > largest_area_size:
                largest_area_size = area_size

# Print the result
print(f'Part 1: {largest_area_size}')
