num = int(input("Enter the number:"))
total = 0
length  = len(str(num))

for i in range(1,length+1):
    rem = num % 10
    total += rem
    num //= 10
    print(total)
print(f"Final total is {total}")

# n = int(input("enter number:"))
# sum = 0

# for i in str(n):
#     print(i)
#     sum += int(i)
# print(f"Final Sum {sum}")
        
    