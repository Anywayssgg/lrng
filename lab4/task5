students = [
    {"name": "Анна", "score": 85, "attempts": 2},
    {"name": "Борис", "score": 55, "attempts": 1},
    {"name": "Виктор", "score": 70, "attempts": 4},
    {"name": "Дарья", "score": 60, "attempts": 3},
]

passed_loop = []
for student in students:
  if student["score"] >= 60 and student["attempts"] <= 3:
    passed_loop.append(student["name"])

print(passed_loop)

passed_comp = [
    student["name"]
    for student in students
    if student["score"] >= 60 and student["attempts"] <= 3
]

print(passed_comp)