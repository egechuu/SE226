import math_utils as mu

dict = {
    'Add' : mu.add, 
    'Substract' : mu.subtract,
    'Multiply' : mu.multiply,
    'Divide' : mu.divide,
    'Power' : mu.power,
    'Mod' : mu.mod
}


if __name__ == "__main__":
    input1 = input("Enter first number: ")
    input2 = input("Enter second number: ")
    operator = input("Enter the operation: ")

    if type(input1) == int and type(input2) == int and operator!= None:
        args = (input1, input2)
        func = dict[operator.lower().capitalize()]
        res = func(*args)
        print(res)
    else:
        print('Enter int values for numbers and a valid operation.')
