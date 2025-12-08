"""
Advent of Code 2025
https://adventofcode.com/2025/day/7
Gemma McLean
"""

# ------
# Read Input
# ------

# List to store grid
grid = []
# Read in the input file and store each line
with open('day07/input.txt') as file_object:
    # Append line as string
    for line in file_object:
        grid.append(line.strip())

# ------
# Preprocessing
# ------

# Get the number of rows and columns
rows = len(grid)
cols = len(grid[0])

# Find the starting position 'S'
start = (0, grid[0].index('S'))


def within_bounds(i, j):
    """
    Checks if the given indices are within the bounds.

    Args:
        i (int): Row index.
        j (int): Column index.

    Returns:
        bool: True if (i, j) is within bounds, False otherwise.
    """
    return 0 <= i < rows and 0 <= j < cols


# ------
# Part 1
# ------

# Count of beam splits
splits = 0
# Initialise a stack with the starting position
stack = [start]
# Set to track visited split nodes
visited = set()

# While there are positions to process
while stack:
    # Pop the last position from the stack
    xy = stack.pop()
    # Extract x and y from tuple
    x = xy[0]
    y = xy[1]
    # Get the next position in the beam's path
    next = grid[x+1][y]
    # Trace downwards until hitting a '^' or going out of bounds
    while next == '.' and within_bounds(x+2, y):
        # Get the next position in the beam's path
        x += 1
        next = grid[x+1][y]
        # If we hit a '^', stop tracing
        if next == '^':
            # Found a split
            split_pos = (x+1, y)
            # Only count this split if we haven't visited it before
            if split_pos not in visited:
                # Increment split count
                splits += 1
                # Mark this position as visited
                visited.add(split_pos)
                # Add new beams to stack
                stack.append((x+1, y-1))
                stack.append((x+1, y+1))
            # Stop tracing this beam
            break

# Print the result
print(f'Part 1: {splits}')
