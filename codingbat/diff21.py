def diff21(n):
    if n > 21:
        # return 2 * (n - 21)
        return 2 * abs(21-n)
    else:
        return 21 - n
    
print(diff21(19))
print(diff21(10))
print(diff21(21))
print(diff21(23))
