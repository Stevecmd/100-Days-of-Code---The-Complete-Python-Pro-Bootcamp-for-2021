names = ["Tim", "Tom", "Tam"]
ages = [20, 25, 32]

students = {}

for key in names:
    for value in ages:
        students[key] = value
        
print(students)
        