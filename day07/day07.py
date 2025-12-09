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
    i = xy[0]
    j = xy[1]
    # Get the next position in the beam's path
    next = grid[i+1][j]
    # Trace downwards until hitting a '^' or going out of bounds
    while next == '.' and within_bounds(i+2, j):
        # Get the next position in the beam's path
        i += 1
        next = grid[i+1][j]
        # If we hit a '^', stop tracing
        if next == '^':
            # Found a split
            split_pos = (i+1, j)
            # Only count this split if we haven't visited it before
            if split_pos not in visited:
                # Increment split count
                splits += 1
                # Mark this position as visited
                visited.add(split_pos)
                # Add new beams to stack
                stack.append((i+1, j-1))
                stack.append((i+1, j+1))
            # Stop tracing this beam
            break

# Print the result
print(f'Part 1: {splits}')

# ------
# Part 2
# ------

# Create a DP grid to store timeline counts, initialised to 0
dp = [[0 for _ in range(cols)] for _ in range(rows)]

# Process grid from bottom to top, right to left
for i in range(rows - 1, -1, -1):
    for j in range(cols - 1, -1, -1):
        # Check if we're at the bottom row
        if not within_bounds(i + 1, j):
            # Reached bottom - this position leads to 1 timeline
            dp[i][j] = 1
        else:
            # Get the next cell in the beam's path (below current)
            next_cell = grid[i + 1][j]
            # Determine timeline count based on next cell type
            if next_cell == '^':
                # Split - sum counts from left and right paths
                dp[i][j] = dp[i + 1][j - 1] + dp[i + 1][j + 1]
            else:
                # Continue - inherit count from cell below
                dp[i][j] = dp[i + 1][j]

# The total timelines is the count at the starting position
result = dp[start[0]][start[1]]
# Print the result
print(f'Part 2: {result}')
