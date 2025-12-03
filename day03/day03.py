"""
Advent of Code 2025
https://adventofcode.com/2025/day/3
Gemma McLean
"""

# List for numbers (battery banks))
nums = []
# Read in the input file and store each number in list
with open('day03/input.txt') as file_object:
    # Get numbers, one per line as strings
    for line in file_object:
        nums.append(line.strip())

# Get length of each number in digits (they are all equal length)
num_length = len(nums[0])

# ------
# Part 1
# ------

# Sum of joltages
total = 0

# Process each number
for num in nums:
    # Greatest digits in positions 1 and 2
    digit1 = '0'
    digit2 = '0'
    # Loop through each digit in the number
    for i in range(num_length):
        # Check if current digit is greater than the current greatest for position 1
        # Also ensure it's not the last digit (position 2 must exist)
        if num[i] > digit1 and i < num_length - 1:
            # Update position 1 greatest
            digit1 = num[i]
            # Get digit at i+1 for position 2
            digit2 = num[i+1]
        # Otherwise, check position 2 only
        else:
            # Check if it's greater than the current greatest for position 2
            if num[i] > digit2:
                # Update position 2 greatest
                digit2 = num[i]
    # Concatenate the two greatest digits, convert to int, and add to total
    total += int(digit1+digit2)

print(f'Part 1: {total}')

# ------
# Part 2
# ------

# Sum of joltages
total = 0

# Process each number
for num in nums:
    # How many digits we are allowed to drop from each number
    # We need to keep 12 digits so we can drop the rest
    drop = num_length - 12
    # Initialise an empty stack
    stack = []
    # Loop through each digit in the number
    for digit in num:
        # While we can still drop digits, and the last digit in the stack
        # is smaller than the current one, pop it to make room for a larger digit.
        while drop > 0 and stack and stack[-1] < digit:
            stack.pop()
            drop -= 1
        # Add the current digit to the stack
        stack.append(digit)
    # If we didn’t remove enough digits in the loop (e.g. already non-increasing),
    # just trim from the end to get exactly k digits
    best = stack[:12]
    # Convert best digits to int and add to total
    total += int(''.join(best))

print(f'Part 2: {total}')
