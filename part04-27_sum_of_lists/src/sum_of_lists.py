# Write your solution here
def list_sum(int1: list, int2: list) -> list:
    list_s = []
    for i, j in zip(int1, int2):
        s = i+j
        list_s.append(s)
    return list_s


# model solution

def list_sum_1(int1: list, int2: list) -> list:
    result = []
    for i in range(len(int1)):
        result.append(int1[i]+int2[i])
    return result


if __name__ == "__main__":
    result = list_sum([1, 2], [1, 2, 3])
    result = list_sum_1([1, 2], [1, 2, 3])
    print(result)
