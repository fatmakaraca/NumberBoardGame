import sys

def board_lst():
    input_file = open(sys.argv[1], "r")
    board = []

    for line in input_file:
        board.append(line.split())
    input_file.close()
    for row in board:
        for number in row:
            print(number + " ", end="")
        print()
    return board


def find_columns(board):
    columns = [[] for _ in range(len(board[0]))]  #Added an empty list equal to the number of columns in the input.

    for row in board:
        for k in range(len(row)):
            columns[k].append(row[k])
    return columns


def is_correct_size(board, cell_index):
    correct_size = True
    if cell_index[0] > (len(board) - 1) or cell_index[1] > (len(board[0]) - 1):
        print("Please enter a correct size!\n")
        correct_size = False
        return correct_size
    elif board[cell_index[0]][cell_index[1]] == " ":
        print("Please enter a correct size!\n")
        correct_size = False
        return correct_size
    else:
        return correct_size


def delete_empty_column_row(board, columns):
    for column in columns:
        empty_column = []
        for _ in range(len(columns[0])):
            empty_column.append(" ")
        if column == empty_column:
            columns.remove(column)  #empty column deleted

    board = [[] for _ in range(len(columns[0]))]
    for column in columns:
        for k in range(len(column)):
            board[k].append(column[k])

    for row in board:
        empty_row = []
        for _ in range(len(board[0])):
            empty_row.append(" ")
        if row == empty_row:
            board.remove(row)  #empty row deleted

    return board


def find_left_cell(board, cell_index):
    row_index, column_index = cell_index[0], cell_index[1]
    if column_index != 0:
        left_cell_coordinate = [row_index, (column_index - 1)]
        return left_cell_coordinate
    else:
        return None


def find_right_cell(board, cell_index):
    row_index, column_index = int(cell_index[0]), int(cell_index[1])
    if column_index != len(board[0]) - 1:
        right_cell_coordinate = [row_index, (column_index + 1)]
        return right_cell_coordinate
    else:
        return None


def find_above_cell(board, cell_index):
    row_index, column_index = cell_index[0], cell_index[1]
    if row_index != 0:
        above_cell_coordinate = [(row_index - 1), column_index]
        return above_cell_coordinate
    else:
        return None


def find_below_cell(board, cell_index):
    row_index, column_index = cell_index[0], cell_index[1]
    if row_index != len(board) - 1:
        below_cell_coordinate = [(row_index + 1), column_index]
        return below_cell_coordinate
    else:
        return None


def checking_neighbors(board, cell_index):
    neighbors = []
    if find_above_cell(board, cell_index) != None:
        neighbors.append(find_above_cell(board, cell_index))

    if find_left_cell(board, cell_index) != None:
        neighbors.append(find_left_cell(board, cell_index))

    if find_right_cell(board, cell_index) != None:
        neighbors.append(find_right_cell(board, cell_index))

    if find_below_cell(board, cell_index) != None:
        neighbors.append(find_below_cell(board, cell_index))

    return neighbors


def is_equal(board, cell_index): #Checks whether neighboring cell is equal to the cell
    equals = []
    neighbors = checking_neighbors(board, cell_index)
    for neighbor in neighbors:
        if board[neighbor[0]][neighbor[1]] == board[int(cell_index[0])][int(cell_index[1])]:
            equals.append(neighbor)
    return equals


def find_all_equals(board, cell_index):  #Returns the indexes of all cells to be deleted
    equals = is_equal(board, cell_index)
    for equal in equals:
        a = is_equal(board, equal)
        for _ in a:
            if _ in equals:
                pass
            else:
                equals.extend(a)

    equals_lst = []
    for k in equals:  #The same elements in the equals list are reduced to one
        if k not in equals_lst:
            equals_lst.append(k)

    equals_lst.sort(key=lambda x: x[1])  #Cells in the same column in the equals list are sorted from top to bottom
    equals_lst.sort(key=lambda x: x[0])  #Cells on the same row in the equals list are sorted from left to right
    movement = True
    if len(equals_lst) == 0:
        print("No movement happened try again\n")
        movement = False

    return equals_lst, movement


def is_game_over(board): #If there are no identical numbers left next to each other on the board, the game is over.

    game_over = True
    for row in board:
        for current_cell in row:
            if current_cell == " ":
                pass
            else:
                current_cell_index = [board.index(row), row.index(current_cell)]
                if len(is_equal(board, current_cell_index)) == 0:
                    continue
                else:
                    game_over = False

    if game_over == True:
        print("Game over")
        sys.exit()
    return game_over


def delete_cells(board, cell_index):
    equals_lst, movement = find_all_equals(board, cell_index)
    if movement is True:
        for equal in equals_lst:
            for row in board[equal[0]:0:-1]:
                board[board.index(row)][equal[1]] = board[board.index(row) - 1][equal[1]]
            board[0][equal[1]] = " "

    board = delete_empty_column_row(board, find_columns(board))
    for row in board:
        for number in row:
            print(number + " ", end="")
        print()
    return board, equals_lst


def main():
    board = board_lst()
    score = 0
    print(f"\nYour score is: {score}\n")
    while is_game_over(board) == False:
        input_cell = input("Please enter a row and a column number: ")
        print()
        input_cell_coordinate = input_cell.split()
        input_cell_index = []
        for i in input_cell_coordinate:
            input_cell_index.append(int(i) - 1)

        if is_correct_size(board, input_cell_index) == True:
            selected_cell_value = board[input_cell_index[0]][input_cell_index[1]]
            board, equals_lst = delete_cells(board, input_cell_index)

            score += len(equals_lst) * int(selected_cell_value)
            print(f"\nYour score is: {score}\n")


if __name__ == '__main__':
    main()



