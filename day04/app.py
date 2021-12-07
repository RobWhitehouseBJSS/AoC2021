# Part 1
calls = []
boards = []
curr_board = []
board_row_counter = 0
called = []
bingo_happened = 0
score = 0
boards_count = 0

# Generate bingo boards
with open("input.txt") as file:
    for line in file.readlines():
        if not calls:
            calls = list(map(int, line.split(",")))

        elif line.strip("\n"):
            board_row_counter += 1
            curr_board.append(list(map(int, line.split())))
            if board_row_counter % 5 == 0:
                boards.append(curr_board)
                board_row_counter = 0
                curr_board = []

boards_count = len(boards)

# After board generation
for call in calls:
    if not bingo_happened:
        called.append(call)
        for board in range(boards_count):
            # Check for row wins
            for row in range(5):
                if not bingo_happened:
                    for rowitem in range(5):
                        if boards[board][row][rowitem] in called and not bingo_happened:
                            if rowitem == 4:
                                bingo_happened = 1
                                winning_board = board
                                winning_call = call
                        else:
                            break
            # Check for column wins
            for column in range(5):
                if not bingo_happened:
                    for colitem in range(5):
                        if boards[board][colitem][column] in called and not bingo_happened:
                            if colitem == 4:
                                bingo_happened = 1
                                winning_board = board
                                winning_call = call
                        else:
                            break

for row in boards[winning_board]:
    for item in row:
        if item not in called:
            score += item

f = open("output.txt", "w")
f.write(f'Part 1: Winning board score - {score * winning_call}\n')

# Part 2
calls = []
boards = []
curr_board = []
board_row_counter = 0
called = []
winning_board = 2000
winning_call = 2000
score = 0
boards_count = 0
boards_left = []

# Generate bingo boards
with open("input.txt") as file:
    for line in file.readlines():
        if not calls:
            calls = list(map(int, line.split(",")))

        elif line.strip("\n"):
            board_row_counter += 1
            curr_board.append(list(map(int, line.split())))
            if board_row_counter % 5 == 0:
                boards.append(curr_board)
                board_row_counter = 0
                curr_board = []

boards_count = len(boards)
boards_left = [b for b in range(boards_count)]

# After board generation
for call in calls:
    if not len(boards_left) == 0:
        called.append(call)
        for board in range(boards_count):
            # Check for row wins
            for row in range(5):
                if not len(boards_left) == 0:
                    for rowitem in range(5):
                        if boards[board][row][rowitem] in called:
                            if rowitem == 4:
                                # print(f"BINGO on board {board} row {row} rowitem {rowitem}!")
                                winning_call = call
                                if board in boards_left:
                                    boards_left.remove(board)
                                if len(boards_left) == 1:
                                    winning_board = boards_left[0]
                        else:
                            break

            # Check for column wins
            for column in range(5):
                if not len(boards_left) == 0:
                    for colitem in range(5):
                        if boards[board][colitem][column] in called:
                            if colitem == 4:
                                # print(f"BINGO on board {board} column {column} colitem {colitem}!")
                                winning_call = call
                                if board in boards_left:
                                    boards_left.remove(board)
                                if len(boards_left) == 1:
                                    winning_board = boards_left[0]
                        else:
                            break

for row in boards[winning_board]:
    for item in row:
        if item not in called:
            score += item

f = open("output.txt", "a")
f.write(f'Part 2: Last winning board score - {score * winning_call}')