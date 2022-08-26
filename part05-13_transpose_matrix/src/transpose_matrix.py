# Write your solution here
def transpose(matrix: list) -> list:

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    print(matrix)


if __name__ == "__main__":
    transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
