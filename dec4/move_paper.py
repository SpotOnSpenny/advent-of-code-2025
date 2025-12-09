# ----- Part 1 -----
# We have to optimize the movement of paper rolls using forklifts in the workshop
# The paper is symbolized as "@" in the input grid
# We can only access a paper roll with a forklift if there is less than 4 other rolls in the adjacent 8 cells
# The answer to part 1 is how many paper rolls we can move in the input grid
# ----- Part 2 -----
# Same as part 1, but now we have to iterate through and actually remove the paper rolls that are movable
# We do this until no more rolls can be moved
# The answer to part 2 is how many total rolls we can move

import os

test_input =[
"............", # Added this row to simplify edge handling
"...@@.@@@@..",
".@@@.@.@.@@.",
".@@@@@.@.@@.",
".@.@@@@..@..",
".@@.@@@@.@@.",
"..@@@@@@@.@.",
"..@.@.@.@@@.",
".@.@@@.@@@@.",
"..@@@@@@@@..",
".@.@.@@@.@..",
"............", # Added this row to simplify edge handling
]

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    input_data = [f".{line.strip()}." for line in f.readlines()]# Add dots at start and end of each line to simplify edge handling
    # add a line of empty dots at the start and end
    row_len = len(input_data[0])
    input_data.insert(0, '.' * row_len)
    input_data.append('.' * row_len)

# Let's get the adjacent positions
adjacent_deltas = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),          (0, 1),
                    (1, -1),  (1, 0), (1, 1)]

def get_adjacent_positions(x, y, input_grid):
    positions_values = []
    for dx, dy in adjacent_deltas:
        nx, ny = x + dx, y + dy
        positions_values.append(input_grid[ny][nx])
    return positions_values

movable_paper_count = 0 
changed_this_iteration = True
iteration = 0
while changed_this_iteration:
    iteration += 1
    print(f"Starting iteration {iteration}")
    after_changes = []
    # I think there's probably a more efficient way to do this rather than nested for loops, but this is easy
    for row_index, row_val in enumerate(input_data):
        if "@" in row_val:
            indices_to_remove = []
            for col_index, col_val in enumerate(row_val):
                if col_val == "@":
                    x = col_index
                    y = row_index
                    adjacent_positions = get_adjacent_positions(x, y, input_data)
                    if adjacent_positions.count("@") < 4:
                        movable_paper_count += 1
                        indices_to_remove.append(col_index)
            # Now we have to remove the paper rolls we found
            new_row = list(row_val)
            for index in indices_to_remove:
                new_row[index] = "."
            new_row = ''.join(new_row)
            after_changes.append(new_row)
        else:
            after_changes.append(row_val)
    if after_changes == input_data:
        changed_this_iteration = False
    else:
        input_data = after_changes

print(f"Total movable paper rolls: {movable_paper_count}")

# ----- Part 1 answer: 1397 -----
# Straightforward nested loop to check each paper roll and its adjacent positions
# Counted how many rolls were present in adjacent positions to see if we could move the roll
#  Got the right answer first try, but would probably be more efficient using dataframes

# ----- Part 2 -----
# Similar to part 1, but this time put it in a while loop and detected changes that were made
# When no changes were made to the grid we stop the loop and get the count
# Again got the right answer first try, but probably could be more efficient using dataframes