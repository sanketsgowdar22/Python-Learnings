student = input("Enter the student name:")
m1 = int(input("Enter the marks of m1:"))
m2 = int(input("Enter the marks of m2:"))
m3 = int(input("Enter the marks of m3:"))
m4 = int(input("Enter the marks of m4:"))
m5 = int(input("Enter the marks of m5:"))
m6 = int(input("Enter the marks of m6:")) 

total = m1+m2+m3+m4+m5+m6
print(f"The total marks of the student {student} is {total}")

percentage = float(total / 6)
print(f"The percentage of the student {student} is {percentage}")

if(percentage > 85):
    print(f"The student {student} has cleared the exam with First class Distinction")
elif(percentage >= 60) and (percentage < 85):
    print(f"The student {student} has cleared the exam with First Class")
elif(percentage >= 45) and (percentage < 60):
    print(f"The student {student} has passed the Exams")
elif(percentage >= 35) and (percentage < 45):
    print(f"The student {student} has just passed the Exams")
else:
    print(f"The student {student} has Failed in the Exams")
