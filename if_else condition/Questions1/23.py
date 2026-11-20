# Write a program to check whether a student has passed or failed (pass marks = 40).

marks = int(input("Enter the marks:"))

if(marks >= 40):
    print(f"Student has passed the exam with {marks} marks")
else:
    print("Student has failed in the exams.")
