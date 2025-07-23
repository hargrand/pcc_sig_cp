"""sample_06_07.py - Dictionary access"""

student = {"name": "Jordan", "age": 18, "grade": "A"}

print(student["name"])
print(student)

student["age"] = 19
print(student)

student["major"] = "Math"
print(student)

del student["grade"]
print(student)
