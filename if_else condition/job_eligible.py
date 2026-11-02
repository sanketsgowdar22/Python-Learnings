graduated = input(("Are you graduated or not(Yes or no):")).lower()
percentage = int(input("Enter your degree percentage:"))
exp = int(input("Enter total experience:"))
python = input("Do you know this language(Yes or no):").lower()

if(graduated == "yes"):
    if(percentage >= 70):
        if(python == "yes"):
            if(exp >= 2):
                print(f"The candidate is eligible for job.")
            else:
                print("Not eligible for the job")
        else:
            print("Not eligible for the job")
    else:
        print("Not eligible for the job")
else:
    print("Candidate is not eligible for the job")
