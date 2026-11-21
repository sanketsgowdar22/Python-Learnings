def even(n):
    if n == 0:
        return
    even(n-1)
    if n > 0:
        if n % 2 == 0:
            print(n)
even(10)

print("*"*20)

def even_num(n):
    if n > 10:
        return
    if n % 2 == 0:
        print(n)
    even_num(n+1)
even_num(1)
    
