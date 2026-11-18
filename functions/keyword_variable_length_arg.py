student_count = 0

def student_details(**details):
    global student_count
    student_count += 1
    print(f"Student {student_count} Details:")
    for key , value in details.items():
        print(f"{key} : {value}") 

no_of_students = int(input("Enter the number of students:"))
for i in range(0,no_of_students):
    print("*"*20)
    name = input("Enter student name:")
    age = int(input("Enter student age:"))
    place = input("Enter the place of student:")
    print("*"*20)
    student_details(name=name,age=age,Place=place)

