"""
Advent of Code 2025
https://adventofcode.com/2025/day/6
Gemma McLean
"""
import math

# ------
# Read Input
# ------

# List to store numbers
nums = []
# List to store raw digit lines
raw = []
# Read in the input file and store in lists
with open('day06/input.txt') as file_object:
    for line in file_object:
        # If first character of line is + or *, it's a line of operators
        if line[0] in '+*':
            # Store operators as list of strings
            operators = (line.strip().split())
        # Otherwise, it's a line of numbers
        else:
            # Append each number line as a list of ints to nums
            nums.append(list(map(int, line.strip().split())))
            # Append the raw digit line to raw
            raw.append(line.rstrip('\n'))

# ------
# Preprocessing
# ------

# Transpose lists to make columns easier to access
nums_t = list(zip(*nums))

# ------
# Part 1
# ------

# Total of sums and products
total = 0
# Loop through operators
for i, op in enumerate(operators):
    # If addition operator
    if op == '+':
        # Sum the corresponding column in nums_t
        result = sum(nums_t[i])
    # If multiplication operator
    elif op == '*':
        # Multiply the corresponding column in nums_t
        result = math.prod(nums_t[i])
    # Add result to total
    total += result

# Print the result
print(f'Part 1: {total}')

# ------
# Part 2
# ------

# ------
# First, find the indices of split points (columns of all spaces)
# ------

# List to store split point indices
split_points = []
# Loop through each character index
for i in range(len(raw[0])):
    # Assume all_space is True initially
    all_space = True
    # Check each row for space at that index
    for j in range(len(raw)):
        # If any row has non-space at that index, mark all_space as False
        if raw[j][i] != ' ':
            all_space = False
            break
    # If all_space is still True, it's a split point
    if all_space:
        # Add index to split_points
        split_points.append(i)

# ------
# Now, split each raw line at the identified split points
# ------

# List to store split lines
split_lines = []
# Loop through each raw line
for raw_line in raw:
    # Split the line in to segments at the identified split points
    segments = []
    # Track the previous index to slice from
    prev_index = 0
    # Loop through each split point
    for split_index in split_points:
        # Slice from previous index to current split point
        segments.append(raw_line[prev_index:split_index])
        # Update previous index to one after current split point
        # This skips the space column
        prev_index = split_index + 1
    # Add the last segment after the final split point
    segments.append(raw_line[prev_index:])
    # Append the list of segments for this line to split_lines
    split_lines.append(segments)

# ------
# Next we convert each number string to a list so we can transpose easily
# ------

# List to store segments as lists of character lists
segment_lists = []
# Loop through each segment in transposed split lines
for segment in list(zip(*split_lines)):
    # Convert each segment string to list of characters and append
    segment_lists.append([list(s) for s in segment])

# ------
# Finally, we can process each segment according to its operator
# ------

# Total of sums and products
total = 0
# Loop through each segment
for i, seg in enumerate(segment_lists):
    # Transpose to get columns of characters
    nums = list(zip(*seg))
    # Join each tuple of chars as a single string and map to int
    joined = [int(''.join(t).rstrip()) for t in nums]
    # Get operator for this segment
    op = operators[i]
    # If addition operator
    if op == '+':
        # Sum the joined numbers
        result = sum(joined)
    # If multiplication operator
    elif op == '*':
        # Multiply the joined numbers
        result = math.prod(joined)
    # Add result to total
    total += result

# Print the result
print(f'Part 2: {total}')
