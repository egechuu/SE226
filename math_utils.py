def add(x,y):
    return x + y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if(y == 0):
        print("You cant dicide by 0.")
        return 
    return x/y

def power(x,y):
    res = x
    for i in range(y-1):
        res *= x
    return res

def mod(x,y):
    return x%y
