"""
Advent of Code 2025
https://adventofcode.com/2025/day/1
Gemma McLean
"""

# Lists for directions and values
dirs = []
vals = []
# Read in the input file and store in lists
with open('day01/input.txt') as file_object:
    for line in file_object:
        # Get direction and value from each line
        dirs.append(line[0])  # First character is the direction
        vals.append(int(line[1:]))  # Remaining characters are the value

# ------
# Part 1
# ------

# Starting position
current = 50
# Number of times position 0 is reached
zero_count = 0

# Process each direction and value
for dir, val in zip(dirs, vals):
    # Subtract or add (then modulo 100) based on direction
    if dir == 'L':
        current = (current - val) % 100
    else:  # dir == 'R'
        current = (current + val) % 100
    # Check if current position is 0
    if current == 0:
        zero_count += 1

# Print the result
print(f'Part 1: {zero_count}')

# ------
# Part 2
# ------

# Starting position
current = 50
# Number of times position 0 is passed or reached
zero_count = 0

# Process each direction and value
for dir, val in zip(dirs, vals):
    # +1 for R, -1 for L
    step = 1 if dir == 'R' else -1
    # Move one click at a time
    for _ in range(val):
        current = (current + step) % 100
        # Check if current position is 0
        if current == 0:
            zero_count += 1

# Print the result
print(f'Part 2: {zero_count}')
