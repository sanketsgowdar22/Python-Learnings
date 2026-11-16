def student_result(*marks):
    total = sum(marks)
    average = total / len(marks)
    maximum = max(marks)
    minimum = min(marks)
    print(f"Total Marks {total}")
    print(f"Average Mraks {average}")
    print(f"Maximum Marks {maximum}")
    print(f"Minimum Marks {minimum}")
    print("-"*20)
    
student_result(80,85,90,90,95)
student_result(70,65,70,77,89)
student_result(88,90,92,97,99,100)
