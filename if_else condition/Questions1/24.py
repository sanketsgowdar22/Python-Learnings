# . Write a program to assign grades:
# •	90+ → A
# •	75–89 → B
# •	50–74 → C
# •	Below 50 → Fail

marks = int(input("Enter the marks:"))

if(1 < marks < 100):
    if(marks >= 90):
        print(f"Student has passed the exam with A grade")
    elif(75 < marks < 89):
        print(f"Student has passed the exam with B grade")
    elif(50 < marks < 74):
        print(f"Student has passed the exam with C grade")
    else:
        print("Student has failed in the exams.")
else:
    print("Invalid marks entered")
