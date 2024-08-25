students = [("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 85), ("Eve", 78), ("Frank", 85), ("Mark", 50), ("George", 21)]


# Extract and print all the unique grades from the list of student scores.
unique_grades = set()
for student in students:
    unique_grades.add(student[1])
print(f"Unique grades: {unique_grades}\n")



# Identify and print the names of the top three students with the highest scores

grade_list = []
for person in students:
    grade_list.append(person[1])


max_grade = []
for i in range(3):
    max_grade.append(max(grade_list))
    grade_list.remove(max(grade_list))


top_three_students = []

for grade in max_grade:
    for student in students:
        if student[1] == grade and student[0] not in top_three_students:
            top_three_students.append(student[0])
            print(student[0], student[1])
            break



# Identify and print the names of students who scored below 51, along with their scores.

for stud in students:
    if stud[1] < 51:
        print(stud[0], stud[1])