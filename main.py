## simple calculator

# Addition
def add(a, b, *args):
    s = 0
    s = a+b
    for i in args:
        s += i  
    return s
    
# Subtraction
def sub(a, b, *args):
    r = 0
    r = a-b
    for i in args:
        r -= i
    return r

# Division
def div(a, b, *args):
    d = 1
    d = a/b
    for i in args:
        d /= i
    return d

# Multiplication
def mul(a, b, *args):
    m = 1
    m = a*b
    for i in args:
        m *= i
    return m

while True:
    n = int(input("Please choose your operation: \n 1:Adition \n 2:Subtraction \n 3:Division \n 4:Multiplication \n"))
    num1 = float(int(input("Enter your first number ")))
    num2 = float(int(input("Enter your second number ")))
    if n==1:
        print('Result: ',add(num1, num2))
        break
    elif n==2:    
        print('Result: ',sub(num1, num2))
        break
    elif n==3:    
        print('Result: ',div(num1, num2))
        break
    elif n==4:    
        print('Result: ',mul(num1, num2))
        break
    else:
        print("wrong Operation")