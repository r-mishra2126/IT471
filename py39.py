class Employee:
    #initialising
    def __init__(self):
        print("employee created")

    def __del__(self):
            print("destructor called, Employee deleted")

obj = Employee()

del obj
