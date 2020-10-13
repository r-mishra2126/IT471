def addition(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def mul(a,b):
    c=a*b
    return c    

def division(a,b):
     c=a/b
     return c


def main():
    a=eval(input("ENTER A: "))
    b=eval(input("ENTER B: "))
    a1=addition(a,b)
    s=sub(a,b)
    m=mul(a,b)
    d=division(a,b)
    print("ADDITION = %d"%a1)
    print("SUBSTRACTION = %d"%s)
    print("MULTIPKICATION = %d"%m)
    print("DIVISION = %f"%d)
main()
