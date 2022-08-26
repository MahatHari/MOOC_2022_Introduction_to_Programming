# Write your solution here
def row_correct(sudoku: list, row_no: int) -> bool:
    row = sudoku[row_no]
    correct = True
    for i in range(len(row)):
        if row[i] == 0:
            continue
        for j in range(i+1, len(row)):
            if row[i] == row[j]:
                correct = False
                break
            else:
                correct = True
        if correct == False:
            break
    return correct

# modal solution


def who_won_v1(sudoku: list, row_no: int) -> bool:
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        number.append(number)
    return True


if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))
