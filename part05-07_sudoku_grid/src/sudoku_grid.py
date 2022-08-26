# Write your solution here

import re


def row_correct(sudoku: list, row_no: int) -> bool:
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
    return True


def column_correct(sudoku: list, column_no: int) -> bool:
    numbers = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in numbers:
            return False
        numbers.append(row[column_no])
    return True


def block_correct(sudoku: list, row_no: int, colum_no: int) -> bool:
    new_list = []
    for row in range(row_no, row_no+3):
        for element in range(colum_no, colum_no+3):
            number = sudoku[row][element]
            if number > 0 and number in new_list:
                return False
            new_list.append(number)
    return True


def sudoku_grid_correct(sudoku: list):
    row_colum = False
    block_check = False
    for i in range(0, 9):
        if row_correct(sudoku, i):
            if column_correct(sudoku, i):
                row_colum = True
            else:
                row_colum = False
                break

    if row_colum:
        for row_no in range(0, 9, 3):
            for colum_no in range(0, 9, 3):
                correct = block_correct(sudoku, row_no, colum_no)
                if correct:
                    block_check = True
                else:
                    return False

    return block_check

# modal solution


def sudoku_grid_correct_v1(sudoku: list) -> bool:
    for row in range(0, 9):
        if not row_correct(sudoku, row):
            return False
    for row in range(0, 9):
        if not column_correct(sudoku, row):
            return False
    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            if not block_correct(sudoku, row, column):
                return False
    return True


if __name__ == "__main__":

    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 6, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [5, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct_v1(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct_v1(sudoku2))
