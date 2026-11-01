# Write a program to check whether a person is eligible to vote (age ≥ 18).

age  = int(input("Enter the age:"))

if (age >= 18):
    print(f"The {age} is eligible to vote")
else:
    print(f"The {age} is not eligible to vote")
