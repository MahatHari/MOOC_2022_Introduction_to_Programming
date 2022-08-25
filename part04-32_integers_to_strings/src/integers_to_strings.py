# Write your solution here


def formatted(my_list: list) -> list:
    result = []
    for num in my_list:
        result.append(str(f"{num:.2f}"))
    return result


if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)
