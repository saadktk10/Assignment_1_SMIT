# Student Marks and Grades
students = {
    "Ali": 85,
    "Sara": 72,
    "Ahmed": 35,
    "Ayesha": 91,
    "Usman": 55
}

def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

passed_count = 0

for name, marks in students.items():
    grade = calculate_grade(marks)
    print(f"Name: {name}, Marks: {marks}, Grade: {grade}")
    
    # Challenge: count how many students passed
    if grade != "Fail":
        passed_count += 1

print(f"\nTotal students passed: {passed_count}")