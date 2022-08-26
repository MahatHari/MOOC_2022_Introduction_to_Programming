# Write your solution here
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


def copy_and_add(sudoku: list, row_no: int, col_no: int, number: int) -> list:
    new_sudoku = []
    for row in sudoku:
        temp = row[:]
        new_sudoku.append(temp)
        # modal solution does above in one line as
        # new_sudoku.append(row[:])

    new_sudoku[row_no][col_no] = number
    return new_sudoku


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
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku_v1(sudoku)
    print()
    print("Copy:")
    print_sudoku_v1(grid_copy)
