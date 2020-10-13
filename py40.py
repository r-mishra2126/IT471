class Employee:
    #initialising
    def __init__(self):
        print("employee created")

    #Calling destructor
    def __del__(self):
        print("Destructor called")

def Create_obj():
    print("Making objects..")
    obj = Employee()
    print("function end..")
    return obj

print("Calling Create_obj() function ")
obj = Create_obj()
print("program end")
del obj
