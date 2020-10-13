def check(n):
    if n<5:
        raise ("Enter value of N>5")

def function():
    try:
        n=eval(input("enter the value of n:>"))
        check(n)
    except ValueError as e:
        print("Value Error:",e)
    else:
        print("value of n is :",n)
    finally:
        print("value of n is printed")
