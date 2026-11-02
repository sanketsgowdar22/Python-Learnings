# n = int(input("Enter the value:"))
# i = 0

# while(i <= n):
#     print(i+i)
#     i += 1
# else:
#     print("Completed")


n = int(input("Enter the value:"))
i = 1
count = 0

while(i <= n):
    count += i
    i += 1
else:
    print(f"The sum of nth value: {count}")
