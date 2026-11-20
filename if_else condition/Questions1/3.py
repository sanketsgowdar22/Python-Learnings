# If ages of Ram, Shyam and Ajay are input through the keyboard, 
# Write a program to determine the youngest of the three.

ram_age = int(input("Enter Rams's Age:"))
shyam_age = int(input("Enter Shyam's Age:"))
ajay_age = int(input("Enter Ajay's Age:"))

if(ram_age < shyam_age) and (ram_age <= ajay_age):
    print("Ram is youngest")
elif(shyam_age < ram_age) and (shyam_age < ajay_age):
    print("Shayam is youngest")
else:
    print("Ajay is youngest")

