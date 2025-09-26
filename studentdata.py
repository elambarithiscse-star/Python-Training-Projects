n = int(input("How many students? "))
students = {}
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    mark = int(input(f"Enter mark of {name}: "))
    students[name] = mark
print("\nDetails: ",students)
topper=max(students,key=students.get)
print(f"Highest mark scorer is {topper} with {students[topper]} marks")