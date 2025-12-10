# ----- Part 1 -----
# We'll be given a list of ranges, and a list of ingredient IDs, separated by a blank line
# Each range is inclusive, and represents the IDs of the ingredients that are fresh
# If an ingredient ID is not in this range it is spoiled
# The answer to part one is how many of the available ingreditns are fresh

# ----- Part 2 -----
# The elves want to know which IDs are fresh
# The answer is how many IDs are fresh

import os

test_ranges = [
    "3-5",
    "10-14",
    "9-12",
    "16-20",  
    "12-18"
]

test_ingredient_ids = [
    "1",
    "5",
    "8",
    "11",
    "17",
    "32"
]

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    sections = f.read().strip().split("\n\n")
    input_ranges = sections[0].strip().split("\n")
    input_ingredient_ids = sections[1].strip().split("\n")

# Some ranges may overlap, so we need to join them first
def merge_ranges(ranges, return_val="lists"):
    # First, sort the ranges by their starting value
    sorted_ranges = sorted(ranges, key=lambda r: int(r.split("-")[0]))
    merged_ranges = []
    current_start, current_end = map(int, sorted_ranges[0].split("-"))
    for range in sorted_ranges[1:]:
        start, end = map(int, range.split("-"))
        # If the start of the current range is within the previous range, we can extend the end if it's bigger
        if start <= current_end:
            current_end = max(current_end, end)
        # If the start of the current range is a new range, then we can add the previous range and start again
        else:
            merged_ranges.append(f"{current_start}-{current_end}")
            current_start, current_end = start, end
    # Add the final range and then sort them all after the merge
    merged_ranges.append(f"{current_start}-{current_end}")
    merged_ranges.sort(key=lambda r: int(r.split("-")[0]))

    # For part 2 we need to return the ranges
    if return_val == "ranges":
        return merged_ranges
    # For part 1 we need to return the sorted lists of firsts and lasts for the binary search
    if return_val == "lists":
        last_digits = [int(r.split("-")[1]) for r in merged_ranges]
        first_digits = [int(r.split("-")[0]) for r in merged_ranges]
        return last_digits, first_digits

# Instead of checking each range, let's use a binary search on the last digit of each range to find the nearest one
def fresh_check(ingredient_id, last_digits, first_digits):
    ingredient_id = int(ingredient_id)

    # If the number is bigger or smaller than the lowest and highest range it's automatically spoiled
    if ingredient_id < first_digits[0] or ingredient_id > last_digits[-1]:
        return False

    # Binary search to find the closest last digit
    low = 0
    high = len(last_digits) - 1
    lowest_delta = 999999999999999999999999999999999999999 # set to an arbitrarily high number
    closest_index = None
    lower_or_higher = None
    while low <= high:
        middle_index = (low + high) // 2
        middle_value = last_digits[middle_index]
        delta = middle_value - ingredient_id
        # If we stumble onto the exact value we can return true because ranges are inclusive
        if ingredient_id == middle_value:
            return True
        # Check if this is the closest delta we've seen so far
        if abs(delta) < abs(lowest_delta):
            lowest_delta = delta
            closest_index = middle_index
            lower_or_higher = "lower" if delta > 0 else "higher"
        # Adjust the search range
        if ingredient_id < middle_value:
            high = middle_index - 1
        elif ingredient_id > middle_value:
            low = middle_index + 1

    # Now we have the closest range, check if the ID is within a neighbouring range to determine freshness
    if lower_or_higher == "lower" and ingredient_id >= first_digits[closest_index]:
        return True
    elif lower_or_higher == "higher" and ingredient_id >= first_digits[closest_index + 1]:
        return True
    return False

# fresh_ingredients = 0
# last_digits, first_digits = merge_ranges(input_ranges, return_val="lists")
# for ingredient_id in input_ingredient_ids:
#     print(f"Checking ingredient ID {ingredient_id}")
#     if fresh_check(ingredient_id, last_digits, first_digits):
#         fresh_ingredients += 1
#         print(f"Ingredient ID {ingredient_id} is fresh")
#     else:
#         print(f"Ingredient ID {ingredient_id} is spoiled")
# print(f"Test fresh ingredients: {fresh_ingredients}")

ranges = merge_ranges(input_ranges, return_val="ranges")
fresh_ids = 0
for range in ranges:
    fresh_ids += int(range.split("-")[1]) - int(range.split("-")[0]) + 1
print("Fresh ID count:", fresh_ids)

# ----- Part 1 Answer: 640 -----
# Tried something new for me to be efficient, writing a binary search to find the nearest range instead of iterating over all of them
# Once we find the nearest range, we just check if the ingredient is within the range (or the range above if it's above the range)
# If it's within the range, it's fresh, and we count it
# Ran into a bit of a problem because I again didn't read the part that said the ranges can OVERLAP so we had to also write a merge function
# to combine overlapping ranges into one before we did the binary search

# ----- Part 2 Answer: 365804144481581 -----
# This was an easy part since we already needed to merge the ranges from part 1
# We just had to sum up and count the total number of IDs within the merged ranges with another loop

# ----- General Notes -----
# Honestly a pretty cool challenge, I liked that I was able to learn something new and implement something
# that I've not had a chance to use before but is common practice in using a binary search for efficiency.
# It was a good exercise in how to think about using these algorithms in daily coding scenarios rather than just
# being a Leetcode andy.

