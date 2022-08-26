# Write your solution here

def factorials(n: int) -> int:
    factorial = {}
    factorial[1] = 1
    multiplier = 1
    for i in range(2, n+1):
        multiplier *= i
        factorial[i] = factorial[i-1]*i
    return factorial


if __name__ == "__main__":
    k = factorials(6)
    print(k[1])
    print(k[3])
    print(k[6])

    j = factorials(5)
    print(j[3])
    print(j[5])
