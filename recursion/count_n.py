# Count the digits in number

def count_n(n):
    count = 0
    if n == 0:
        return 0 
    count += 1
    return count+count_n(n//10) 

n = int(input("Enter the number:"))
if n == 0:
    result = 1
else:
    result = count_n(n)
print(result)
