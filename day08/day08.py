"""
Advent of Code 2025
https://adventofcode.com/2025/day/8
Gemma McLean
"""
import math

# ------
# Read Input
# ------

# List for positions of junction boxes in 3D space
positions = []
# Read in the input file and store each position in list
with open('day08/input.txt') as file_object:
    # Get position as a list of ints [x,y,z]
    for line in file_object:
        positions.append([int(coord) for coord in line.strip().split(',')])

# ------
# Preprocessing
# ------

# Empty list to store dictionaries of pairs (indices) and their Euclidean distance
distances = []
# Calculate Euclidean distances between each unique pair of junction boxes
for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        # Get positions of the two junction boxes
        pos1 = positions[i]
        pos2 = positions[j]
        # Calculate Euclidean distance
        distance = ((pos1[0] - pos2[0]) ** 2 +
                    (pos1[1] - pos2[1]) ** 2 +
                    (pos1[2] - pos2[2]) ** 2) ** 0.5
        # Store pair of indices and their distance in a dictionary
        pairs = {(i, j): distance}
        # Append to distances list
        distances.append(pairs)
# Sort distances by value (with largest first so we can easily pop smallest)
distances.sort(key=lambda x: list(x.values())[0], reverse=True)


def init_circuits():
    """
    Initialise the circuits list with each junction box in its own set.

    Returns:
        list: List of sets, each containing one junction box index.
    """
    circuits = []
    for i in range(len(positions)):
        circuits.append({i})
    return circuits


def merge_circuits(circuits, closest_pair):
    """
    Merge the circuits containing the two given junction box indices.

    Args:
        circuits (list): List of sets representing circuits.
        closest_pair (dict): Dictionary with a tuple of two indices as key.
    """
    # Get the indices of the junction boxes in this pair
    pair_indices = list(closest_pair.keys())[0]
    idx1, idx2 = pair_indices
    # Find the circuits that contain these indices
    for circuit in circuits:
        if idx1 in circuit:
            circuit1 = circuit
        if idx2 in circuit:
            circuit2 = circuit
    # If they are different circuits, merge them (if not, do nothing)
    if circuit1 is not circuit2:
        circuit1.update(circuit2)
        circuits.remove(circuit2)


# ------
# Part 1
# ------

# The target number of connections we want to make
num_connections = 1000
# Get our initial circuits list
circuits_part1 = init_circuits()
# Use a copy so we don't modify the original distances list
distances_part1 = distances.copy()

# Process until we have the required number of connections
for i in range(num_connections):
    # Get closest pair (smallest distance)
    closest_pair = distances_part1.pop()
    # Merge the circuits containing this pair
    merge_circuits(circuits_part1, closest_pair)

# Sort circuits by length of the sets (largest first)
circuits_part1.sort(key=lambda x: len(x), reverse=True)
# Get 3 largest circuits
largest_circuits = circuits_part1[:3]
# Calculate product of their sizes
product = math.prod(len(circuit) for circuit in largest_circuits)
# Print the result
print(f'Part 1: {product}')

# ------
# Part 2
# ------

# Get our initial circuits list
circuits_part2 = init_circuits()
# Use a copy so we start fresh
distances_part2 = distances.copy()

# Process until we have only one circuit
while len(circuits_part2) > 1:
    # Get closest pair (smallest distance)
    closest_pair = distances_part2.pop()
    # Merge the circuits containing this pair
    merge_circuits(circuits_part2, closest_pair)

# Get indices of the last two connected junction boxes (last value of closest_pair)
pair_indices = list(closest_pair.keys())[0]
idx1, idx2 = pair_indices
# Print the product of their x coordinates
print(f'Part 2: {positions[idx1][0] * positions[idx2][0]}')
