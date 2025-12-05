"""
Advent of Code 2025
https://adventofcode.com/2025/day/2
Gemma McLean
"""

# ------
# Read Input
# ------

# List to store ranges
ranges = []
# Read in the input file and store in list
with open('day02/input.txt') as file_object:
    # Get ranges separated by commas
    for r in file_object.readline().strip().split(','):
        # Append each range as a tuple of ints
        ranges.append(tuple(map(int, r.split('-'))))

# ------
# Part 1
# ------

# Count of invalid IDs
invalid_ids = 0

# Process each range
for start, end in ranges:
    # Check each number in the range
    for i in range(start, end + 1):
        # Convert number to string for easier digit access
        num_str = str(i)
        # Check whether the length of the number is even
        # If it's odd, we don't even need to check it as it can't be invalid
        if len(num_str) % 2 == 0:
            # Split num_str in half
            mid = len(num_str) // 2
            first_half = num_str[:mid]
            second_half = num_str[mid:]
            # Check if both halves are the same
            if first_half == second_half:
                # If they are, add number to invalid count
                invalid_ids += i

# Print the result
print(f'Part 1: {invalid_ids}')

# ------
# Part 2
# ------

# Count of invalid IDs
invalid_ids = 0

# Process each range
for start, end in ranges:
    # Check each number in the range
    for i in range(start, end + 1):
        # Convert number to string for easier digit access
        num_str = str(i)
        # Check each possible group size from half the length down to 1
        for j in range(len(num_str)//2, 0, -1):
            # If the length of the number is divisible by the group size
            if len(num_str) % j == 0:
                # Split num_str into groups of size j
                groups = [num_str[k:k + j] for k in range(0, len(num_str), j)]
                # Check if all groups are the same
                if all(group == groups[0] for group in groups):
                    # If they are, add number to invalid count and break
                    invalid_ids += i
                    break

# Print the result
print(f'Part 2: {invalid_ids}')
