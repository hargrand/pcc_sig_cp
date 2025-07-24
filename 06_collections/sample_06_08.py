"""sample_06_07.py - Dictionary access"""

student = {"name": "Jordan", "age": 18, "grade": "A"}

print(student.get("name"))
print(student.get("address"))
print(student.get("address", "dunno"))


print(tuple(student.keys()))
print(set(student.values()))
print(list(student.items()))

for key, value in student.items():
    print(key, value)
