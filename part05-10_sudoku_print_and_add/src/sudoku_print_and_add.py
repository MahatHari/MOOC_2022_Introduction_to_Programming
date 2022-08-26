# Write your solution here

def print_sudoku(sudoku: list):
    new_row = 0
    new_column = 0
    for row in range(9):
        for element in range(9):
            if sudoku[row][element] == 0:
                sudoku[row][element] = "_"

    for new_row in range(9):
        if new_row > 0 and new_row % 3 == 0:
            print()
        for new_column in range(9):
            print(sudoku[new_row][new_column], end=" ")
            if (new_column+1) % 3 == 0:
                print(end=" ")
        print()

# modal solution for printing


def print_sudoku_v1(sudoku: list):
    r = 0  # count row
    for row in sudoku:
        s = 0  # count column
        for character in row:
            s += 1  # increaase column by 1
            if character == 0:
                character = "_"
            m = f"{character} "
            # after 3 column add space
            if s % 3 == 0 and s < 8:
                m += " "
            print(m, end="")
        # go to new line
        print()
        # increase row count after space
        r += 1
        if r % 3 == 0 and r < 8:
            print()


def add_number(sudoku: list, row_no: int, col_no: int, number: int):
    sudoku[row_no][col_no] = number


if __name__ == '__main__':

    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku_v1(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
