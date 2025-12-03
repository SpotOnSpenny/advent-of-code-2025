# ----- Part 1 -----
# Need to check product ID ranges for validity
# Will appear as a list of ranges (ex 11-22)
# Each range comma separated, two numbers separated by a hyphen, and are inclusive
# Invalid ID if ONLY contains numbers repeated TWICE (ex 6464, 55, 1212)
# Answer to the puzzle is the SUM of all the INVALID ids

# ----- Part 2 -----
# Same as part 1, but now invalid IDs are any that repeat at LEAST twice (ex 1212, 5555, 111)

import os

def parse_range(range_str):
    start, end = map(int, range_str.split('-'))
    return range(start, int(end) + 1)

def check_id_validity(product_id):
    # Convert to string for parsing
    id_str = str(product_id)
    length = len(id_str)

    # Check to see what numbers the ID is divisible by
    possible_splits = [i for i in range(1, length // 2 + 1) if length % i == 0]

    # Split the string into chunks and check for repetition
    for split_size in possible_splits:
        chunk = id_str[:split_size]
        repetitions = length // split_size
        if chunk * repetitions == id_str:
            return False  # Invalid ID
    return True  # Valid ID

test_input = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224",
"1698522-1698528","446443-446449","38593856-38593862","565653-565659",
"824824821-824824827","2121212118-2121212124"]

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    input_data = f.read().strip().split(',')

invalid_sum = 0
for range_str in input_data:
    id_range = parse_range(range_str)

    for product_id in id_range:
        if not check_id_validity(product_id):
            print("Invalid ID found:", product_id)
            invalid_sum += product_id
print("Sum of invalid IDs:", invalid_sum)

# ----- Part 1 Answer 32976912643 -----
# Used one function to parse the range strings into iterables and another to check validity of each ID in the range
# The validity check function is faster by checking only even splits since we only care if its repeated twice
# If it is divisible, we check to see if the first half repeated equals the full ID, if it does it's invalid
# Summed the invalid IDs as they were found

# ----- Part 2 Anser 54446379122 -----
# We actually did this first because we didn't read the question closely enough (oops)
# Just had to modify the validity check function to first determine possible splits based on id size
# Then check the if the split multiplied by the number of repetitions equals the full ID, if it does it's invalid
# Summed up the invalids as before