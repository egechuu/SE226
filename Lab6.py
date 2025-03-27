
#Q1
from math import radians


def factorial(x):
    if(x==1 or x== 0):
        return 1
    else:
        return factorial(x-1)*x

print(factorial(5))

#Q2 
lambdaFunc = lambda x,n : pow(-1,n)*pow(x,2*n+1)/factorial(2*n+1)

def sine_x(x, n):
    sum = 0
    x = radians(x)
    for i in range(n):
        sum += lambdaFunc(x,i)
        print(sum)

#sine_x(90, 20)

#Q3 

res = 0

def func(n):
    """
    This function computes the sum of the series 1 + 1/2 + 1/3 + ... + 1/n recursively.
    It updates the global variable `res` to store the cumulative result.
    """

    global res
    
    #if n is 0, reset the result to 0
    if n == 0:
        return
    
    #add the current term (1/n) to res
    else:
        res += 1/n
    
    #recursively call the function for n-1
    func(n-1)

func(4)
print(res)

