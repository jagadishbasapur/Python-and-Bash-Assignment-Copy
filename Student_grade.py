student = {
    "Jagadish": "A",
    "ABC": "B",
    "XYZ": "C"
}

print("student grade:", student)

name = input("Enter student name: ")
grade = input("Enter grade: ")

if name in student:
    student[name] = grade
    print("student grade updated successfully")
else:
    student[name] = grade
    print("student grade added successfully")

print("\nAll student grades:")
#for name, grade in student.items():
 #   print(name, ":", grade)