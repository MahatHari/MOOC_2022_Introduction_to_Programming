
def exam_and_exercise_points(inputs: str) -> list:
    splitted_str = inputs.split(" ")
    return [int(splitted_str[0]), int(splitted_str[1])]


def get_exercise_points(inputs: int) -> int:
    return inputs//10


def grade_points(points: int) -> int:
    grade_boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= grade_boundary[i]:
            return i


def mean(points: list) -> float:
    return sum(points)/len(points)


def main():
    points = []
    grades = [0]*6
    while True:
        inputs = input("Examp points and exercises completed: ")
        if inputs == "":
            break
        exam_and_exercise = exam_and_exercise_points(inputs)
        exercise_points = get_exercise_points(exam_and_exercise[1])
        total_points = (exam_and_exercise[0])+exercise_points
        points.append(total_points)
        grade = grade_points(total_points)

        if exam_and_exercise[0] < 10:
            grade = 0
        grades[grade] += 1

        pass_percentage = 100*(len(points)-grades[0])/len(points)

    print("Statistics:")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars = "*" * grades[i]
        print(f"  {i}: {stars}")


main()
