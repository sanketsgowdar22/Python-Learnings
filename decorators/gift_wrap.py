# Without using @my_decorator 
def my_decorator(func):
    def wrapper():
        print("Before Calling Function")
        func()
        print("After Calling Function")
    return wrapper

def gift():
    print("Welcome to Decorators")
    
result = my_decorator(gift)
print(result())

print("*"*30)

#With using @my_decorator
def my_decorator(func):
    def wrapper():
        print("Before Calling Function")
        func()
        print("After Calling Function")
    return wrapper

@my_decorator
def gift():
    print("Welcome to Decorators")
gift()


