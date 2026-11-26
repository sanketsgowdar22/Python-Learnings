temp = [22,28,35,19]

def cecl_fahren(temp):
    result = []
    for i in temp:
        fahrenheit = ((i * (9/5)) + 32)
        result.append(fahrenheit)
    return result

print(cecl_fahren(temp))

print("*"*20)

fahrenheit = map(lambda i: ((i * 9/5)+32) , temp)
print(list(fahrenheit))  
