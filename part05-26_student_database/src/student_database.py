def add_student(students: dict, name: str):
    students[name] = {}
    students[name]["courses"] = []
    students[name]["average"] = 0.0


def print_student(students: dict, student_name: str):
    if student_name in students:
        print(f"{student_name}:")
        completed_courses = students[student_name]["courses"]
        if len(completed_courses) == 0:
            print(" no completed courses")
        else:
            print(f" {len(completed_courses)} completed courses: ")
            for course in completed_courses:
                print(f"  {course[0]} {course[1]}")
            average_grade = students[student_name]["average"]
            print(f" average grade {average_grade}")
    else:
        print(f"{student_name}: no such person in the database")


def add_course(students: dict, student_name: str, course: tuple):
    if student_name in students:
        completed_courses = students[student_name]["courses"]
    # check if course has grade 0
        valid_course = course[1] != 0
        if valid_course:
            # check if course name  already exist
            already_exists = False
            grade_higher = False
            existing_course = None
            for completed_course in completed_courses:
                if completed_course[0] == course[0]:
                    already_exists = True
                    if completed_course[1] < course[1]:
                        grade_higher = True
                        existing_course = completed_course

            if not already_exists:
                students[student_name]["courses"].append(course)
            # course already exist, check for grades
            # grades higher than stored, replace
            if already_exists and grade_higher:
                course_position = students[student_name]["courses"].index(
                    existing_course)
                students[student_name]["courses"][course_position] = course


def get_average(students: dict, student: str):
    grade = 0
    for student in students:


def summary(students: dict):
    num_students = len(students)
    most_course_completed = 0
    most_course_completing_student = None
    best_average = 0.0
    best_average_student = None
    print(f"students {num_students}")
    for student in students:

        courses_each = len(students[student]["courses"])

        if courses_each > most_course_completed:
            most_course_completed = courses_each
            most_course_completing_student = student
        if students[student]["average"] > best_average:
            best_average = students[student]["average"]
            best_average_student = student

    print(
        f"most course completed {most_course_completed} {most_course_completing_student}")
    print(f"best average grade {best_average} {best_average_student}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    print_student(students, "Peter")
