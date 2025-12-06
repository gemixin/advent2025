"""
Advent of Code 2025
https://adventofcode.com/2025/day/5
Gemma McLean
"""

# ------
# Read Input
# ------

# List to store ranges
ranges = []
# List to store IDs to check
ids = []
# Read mode
read_ranges = True
# Read in the input file and store in lists
with open('day05/input.txt') as file_object:
    for line in file_object:
        # Switch read mode on blank line
        if line == '\n':
            read_ranges = False
            continue
        # Read ranges when in range mode
        if read_ranges:
            # Get ranges separated by commas
            for r in line.strip().split(','):
                # Append each range as a list of ints
                ranges.append(list(map(int, r.split('-'))))
        # Read IDs when not in range mode
        else:
            # Append each ID as int
            ids.append(int(line.strip()))

# ------
# Preprocessing
# ------

# Sort ranges by start value
ranges.sort(key=lambda x: x[0])
# List to store merged ranges in sorted, non-overlapping order
# Populate with initial range
merged = [ranges[0]]

# Merge overlapping or touching ranges
for s, e in ranges[1:]:
    # Get the last (most recent) merged range
    last_s, last_e = merged[-1]
    # If the current range starts after the last merged one ends + 1,
    # they don't overlap or touch
    if s > last_e + 1:
        # Add as new range
        merged.append([s, e])
    # Otherwise, they do overlap or touch
    else:
        # Merge by extending the end of the last merged range to the max end
        merged[-1][1] = max(last_e, e)

# ------
# Part 1
# ------

# Count of fresh IDs
fresh = 0
# Loop through our IDs and check if they are fresh
for id in ids:
    # Check each range
    for start, end in merged:
        # If ID is within any range, it's fresh
        if start <= id <= end:
            # Increment fresh count and stop checking ranges
            fresh += 1
            break
        # If ID is less than end of current range, we can stop checking
        # This is because our ranges are sorted and non-overlapping
        if id < end:
            break

# Print the result
print(f'Part 1: {fresh}')

# ------
# Part 2
# ------

# Sum the sizes of merged ranges
count = sum(e - s + 1 for s, e in merged)
# Print the result
print(f'Part 2: {count}')
