# ----- Part 1 -----
# We have to perform mathematical operations done funkily by cephalopods
# The problems appear as vertical columns, and either a + or * in the last line indicating what to do with the numbers in that column
# The answer is the sum of all results for each column

# ----- Part 2 -----
# Cephalopod math is INSANE
# Each number is given as a COLUMN within the column, with the most siginficant digit at the top
# So we have to perform the same operations, but parse out the values differently
# The answer is still the sum of all results from each column operation 

import os
import pandas

test_input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +   
"""

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    input_data = f.read().strip()

# I think the easiest way to start here is to convert the input from a text string into a dataframe
# This will let us easily access and work with the columns
def input2dataframe(input_str):
    input_lines = input_str.split("\n")
    if input_lines[0] == "":
        input_lines = input_lines[1:]
    if input_lines[-1] == "":
        input_lines = input_lines[:-1]

    length_between_operands = []
    space_count = 0
    for index, character in enumerate(input_lines[-1]):
        if character == " ":
            space_count += 1
        # If we are the at the end of the row then we should also record the space count
        if index == len(input_lines[-1]) -1:
            space_count += 2 # add one for the space, and one for the operand
            length_between_operands.append(space_count)
        elif input_lines[-1][index + 1] != " ":
            length_between_operands.append(space_count)
            space_count = 0
    print(f"Lengths between operands: {length_between_operands}")
    operations = []
    # we can build out the digits we'll operate on now
    for length in length_between_operands:
        column = [line[:length] for line in input_lines]
        # Remove the used characters from each line plus the space in between columns
        input_lines = [line[length + 1:] for line in input_lines]
        operations.append(column)

    return operations

# The actual mathematical operations can occur here
def operate_column(column):
    operation = column[-1].strip()
    numbers = []
    i = len(column[0]) - 1
    number = []
    while i >= 0:
        for line in column[:-1]:
            if line[i] != " ":
                number.append(line[i])
        i -= 1
        print(f"Built number: {number}")
        numbers.append(int("".join(number)))
        number = []
    print(f"Operating on numbers: {numbers} with operation: {operation}")

    if operation == "+":
        return sum(numbers)
    elif operation == "*":
        result = 1
        for num in numbers:
            result *= num
        return result
    else:
        print(column)
        raise ValueError(f"Unknown operation: {operation}")

total_result = 0
# transpose the dataframe to make columns easier to iterate over
input_list = input2dataframe(input_data)
for operation in input_list:
    print(operation)
    col_result = operate_column(operation)
    print(f"Column result: {col_result}")
    total_result += col_result

print(f"Total result: {total_result}")

# ----- Part 1 Answer: 4648618073226 -----
# Was fairly simple, especially working with dataframes which is something I'm very familiar with
# Transposed the dataframe to make the column operations easier, and simply added the results

# ----- Part 2 Answer: 7329921182115 -----
# I had a lot of trouble parsing the columns the way that part two wants us to
# I ended up abandoning the dataframe approach and working with lists of strings instead
# I actually walked away for a little bit frustrated, but eventually realized that the number of numbers we need to operate
# on is equal to the number of characters in the operations line, so I used that to separate out the numbers we need for each operation
# From there we took the number at each index from each line as a way to build out the full number for that column and operated accordingly
# Got there in the end, but was frustarting for a bit!