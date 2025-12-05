"""
Advent of Code 2025
https://adventofcode.com/2025/day/4
Gemma McLean
"""
from collections import deque

# ------
# Read Input
# ------

# List to store grid
grid = []
# Read in the input file and store each line
with open('day04/input.txt') as file_object:
    # Append line as string
    for line in file_object:
        grid.append(line.strip())

# ------
# Preprocessing
# ------

# Get the number of rows and columns
rows = len(grid)
cols = len(grid[0])

# Possible directions (8 neighbours)
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


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


def get_neighbour_counts(grid):
    """
    Gets the count of neighbouring rolls for each roll ('@') in the grid.

    Args:
        grid (list of str): The grid representing the rolls.

    Returns:
        neighbour_counts (list of list of int): A grid where each element represents
        the count of neighbouring rolls for the corresponding position in the grid.
    """
    # Create an empty grid to store neighbour counts
    neighbour_counts = [[0] * cols for _ in range(rows)]

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the cell contains a roll ('@'), count its neighbours
            if grid[i][j] == '@':
                count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if within_bounds(ni, nj) and grid[ni][nj] == '@':
                        count += 1
                # Store the count in the neighbour_counts grid
                neighbour_counts[i][j] = count

    # Return the grid of neighbour counts
    return neighbour_counts


def get_accessible_rolls(grid, neighbour_counts):
    """
    Gets a queue of accessible rolls (with fewer than 4 neighbours).

    Args:
        grid (list of str): The grid representing the rolls.
        neighbour_counts (list of list of int): A grid where each element represents
        the count of neighbouring rolls for the corresponding position in the grid.

    Returns:
        accessible_rolls (queue): A queue of tuples representing the positions of
        accessible rolls in the grid.
    """
    # Create a queue to store accessible rolls
    queue = deque()

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the cell contains a roll ('@') and has < 4 neighbours, add to queue
            if grid[i][j] == '@' and neighbour_counts[i][j] < 4:
                queue.append((i, j))

    # Return the queue of accessible rolls
    return queue


# Count the neighbouring rolls for each roll in the grid
neighbour_counts = get_neighbour_counts(grid)
# Get the accessible rolls (with fewer than 4 neighbours)
accessible_rolls = get_accessible_rolls(grid, neighbour_counts)

# ------
# Part 1
# ------

# Print the result, which is simply the length of the accessible rolls queue
print(f'Part 1: {len(accessible_rolls)}')

# ------
# Part 2
# ------

# Convert grid to a list of lists for mutability
grid = [list(row) for row in grid]
# Count of removed rolls
removed = 0

# While the queue is not empty
while accessible_rolls:
    # Get the next accessible roll
    i, j = accessible_rolls.popleft()
    # Remove this roll
    grid[i][j] = '.'
    removed += 1

    # Update neighbours
    for di, dj in directions:
        ni, nj = i + di, j + dj
        # If neighbour is a roll and not already accessible
        if (within_bounds(ni, nj)
            and grid[ni][nj] == '@'
                and (ni, nj) not in accessible_rolls):
            # Decrease its neighbour count
            neighbour_counts[ni][nj] -= 1
            # If it now has fewer than 4 neighbours, add to accessible rolls
            if neighbour_counts[ni][nj] < 4:
                accessible_rolls.append((ni, nj))

# Print the result
print(f'Part 2: {removed}')
