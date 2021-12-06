#%%
NUMBER = "number"
WAS_DRAWN = "was_drawn"


def get_input():
    with open("./04_input.txt") as file:
        drawn_numbers = [int(number) for number in file.readline().split(",")]
        file.readline()

        boards = []
        for i in range(100):
            board = []
            for j in range(5):
                board.append(
                    [
                        {NUMBER: int(x), WAS_DRAWN: False}
                        for x in file.readline().split()
                    ]
                )
            boards.append(board)
            file.readline()

    return drawn_numbers, boards


#%%
drawn_numbers, boards = get_input()


def play_game():
    for drawn_number in drawn_numbers:
        for board in boards:
            for row in board:
                for entry in row:
                    if entry[NUMBER] == drawn_number:
                        entry[WAS_DRAWN] = True

            has_complete_row, has_complete_col = False, False
            for row in board:
                if all(entry[WAS_DRAWN] for entry in row):
                    has_complete_row = True
                    break
            for col in range(5):
                if all(board[i][col][WAS_DRAWN] for i in range(5)):
                    has_complete_col = True
                    break

            if has_complete_row or has_complete_col:
                return drawn_number, board


last_drawn_number, winning_board = play_game()
answer_part_one = 0

for row in winning_board:
    answer_part_one += sum(x[NUMBER] for x in row if not x[WAS_DRAWN])

answer_part_one *= last_drawn_number
answer_part_one

#%%
drawn_numbers, boards = get_input()


def play_game_2():
    winning_boards = []
    remember_drawn_number = 0
    for drawn_number in drawn_numbers:
        for board_idx, board in enumerate(boards):
            for row in board:
                for entry in row:
                    if entry[NUMBER] == drawn_number:
                        entry[WAS_DRAWN] = True

            if board_idx in winning_boards:
                continue

            has_complete_row, has_complete_col = False, False
            for row in board:
                if all(entry[WAS_DRAWN] for entry in row):
                    has_complete_row = True
                    break
            for col in range(5):
                if all(board[i][col][WAS_DRAWN] for i in range(5)):
                    has_complete_col = True
                    break

            if has_complete_row or has_complete_col:
                winning_boards.append(board_idx)
                remember_drawn_number = drawn_number

            if len(winning_boards) == 100:
                return remember_drawn_number, boards[board_idx]


number, board = play_game_2()
answer_part_two = 0

for row in board:
    answer_part_two += sum(x[NUMBER] for x in row if not x[WAS_DRAWN])

answer_part_two *= number
answer_part_two
