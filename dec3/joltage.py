# ----- Part 1 -----
# Batteries are arranged into banks, each line of the input is a bank
# Each battery has a joltage rating, which is a number from 1-9
# Need to turn on exactly 2 batteries in each bank, the joltage formed is equal to the number formed by the two digits
# Need to find the largest possible joltage from each bank, and then sum these for the answer

# ----- Part 2 -----
# The same as part 1, except now we need the biggest 12 digit number instead of 2 digit number

import os

test_input = [
"987654321111111",
"811111111111119",
"234234234234278",
"818181911112111",
]

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    input_data = [line.strip() for line in f.readlines()]

def max_joltage(bank):
    digits = []
    start = 0

    for i in reversed(range(12)):
        digits.append(max(int(character) for character in bank[start:-i if -i != 0 else None]))
        start = bank.index(str(digits[-1]), start) + 1

        #if the digits left are exactly equal to the number we need, take them all
        remaining_needed = 12 - len(digits)
        if len(bank[start:]) == remaining_needed and i != 0:
            digits.append(bank[start:])
            break

    joltage = int(''.join(map(str, digits)))
    print(f"Max joltage for bank {bank} is {joltage}")
    return joltage

combined_joltage = sum(max_joltage(bank) for bank in input_data)
print(f"Combined joltage for test input: {combined_joltage}")

# ----- Part 1 Answer 17109 -----
# Pretty straightforward answer, just took everything except the last character and found the biggest digit
# Couldn't be the last character because we need two digits to form the joltage, but if we just took the 10 spot
# first as the biggest one, it doesn't matter what the last digit is, it will always be the biggest possible
# Then we only search from that digit forward for the second digit to be efficient

# ----- Part 2 answer 169347417057382 -----
# Same as part 1, but instead of hard coding digit 1 and digit 2, we looped through a reversed range to find all 12 digits
# This would work as is, but also just for fun added a check to see if the remaining digits were equal to what was left in the bank
# If they were, we can just take them all at once instead of looping through some iterations. This probably helped save
# a few loops and was more efficient overall.