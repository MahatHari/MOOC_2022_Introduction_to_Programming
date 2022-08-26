# Write your solution here
def times_ten(start_index: int, end_index: int) -> dict:
    times = {}
    for i in range(start_index, end_index+1):
        times[i] = i*10

    return times


if __name__ == "__main__":
    print(times_ten(3, 6))
