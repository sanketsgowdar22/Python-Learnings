# n = int(input("enter number:"))
# temp = n
# i = 1
# total = 0
# while(n > 0):
#     rem = n%10
#     fact = 1
#     while(i <= rem):
#         fact=fact * i
#         i += 1
#     total+=fact
#     n//=10
# if(total == temp):
#     print("Strong")
# else:
#     print("Not Strong")


n=int(int(input("....")))
temp=n
total=0
while n>0:
    rem=n%10
    fact=1
    i=1
    while i<=rem:
        fact*=i
        i+=1
    total+=fact
    n//=10
if total==temp:
    print("yes")
else:
    print("no")

