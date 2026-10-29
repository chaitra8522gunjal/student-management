
students = []


def add_student(name, marks):
    if not name.strip():
        raise ValueError("Student name cannot be empty")

    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100")

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    return student

# Determines whether a student passes or failsgit add student.py

def get_result(marks):
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100")

    if marks >= 35:
        return "Pass"

    return "Fail"


if __name__ == "__main__":
    add_student("Riya", 85)
    add_student("Amit", 28)

    for student in students:
        result = get_result(student["marks"])
        print(
            f'{student["name"]}: '
            f'{student["marks"]} marks - {result}'
        )
