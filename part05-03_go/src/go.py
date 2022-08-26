# Write your solution here
def who_won(game_board: list) -> int:
    countA = 0
    countB = 0
    for row in game_board:
        for cell in row:
            if cell == 1:
                countA += 1
            elif cell == 2:
                countB += 1
            else:
                continue
    if countA > countB:
        return 1
    elif countB > countA:
        return 2
    else:
        return 0


if __name__ == "__main__":
    print(who_won([[1, 2, 2], [1, 1, 2], [2, 2, 2], [1, 1, 1]]))
