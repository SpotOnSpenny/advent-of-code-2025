import os

def move_lock(start, movement_string):
    # First, parse the input of the movement string
    movement_direction = "Left" if movement_string[0] == 'L' else "Right" if movement_string[0] == 'R' else None
    if movement_direction is None:
        raise ValueError("Invalid movement string. Must start with 'L' or 'R'.")
    try:
        movement_steps = int(movement_string[1:])
    except ValueError:
        raise ValueError("Invalid movement string. Steps must be an integer.")
    
    passed_zero = 0
    # Calculate the new position based on direction and steps
    match movement_direction:
        case "Left":
            new_position = (start - movement_steps)
            while new_position < 0:
                new_position += 100
                passed_zero += 1
            if new_position == 0:
                passed_zero += 1
            if start == 0:
                passed_zero -= 1
        case "Right":
            new_position = (start + movement_steps)
            while new_position > 99:
                new_position -= 100
                passed_zero += 1
    return new_position, passed_zero 

# Take the input.txt file and read it into a list of strings
with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

test_input = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

# Set up the puzzle input
position = 50
zero_count = 0
for step in puzzle_input:
    position, passed_zero = move_lock(position, step)
    zero_count += passed_zero
    print(f"Moved {step}, new position is {position}, passed zero {passed_zero} times.")
print(f"Number of times position was zero: {zero_count}")

# ----- Part 1 Answer 1066 -----
# The answer to part 1 is the number of times the position was zero
# Used a simple counter to track how many times new new position was 0 after the rotation

# ----- Part 2 Answer 6223 -----
# The anser to part 2 is the number of times the position ever passed zero during the input steps
# Added in a counter to track how many times we passed zero during the movements
# Used the calculations we were already doing to set the dial between 0-99 as an indicator of passing zero
# Also had to account for the edge case where zero was the start, because moving left from here would require the calculation
# we checked for, but this is not a new passing of zero and should not be counted