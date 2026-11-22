di = {"Name":"Sanket","RollNo":34,"Class":"10A","Marks":64}

print(di["Name"])
print(di.keys())
print(di.values())
print(di.items())
print(di.get("Name"))

print("*"*20)

for key,value in di.items():
    print(key,"-"*5,value)
