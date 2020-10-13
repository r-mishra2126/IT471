class employee:
     def __init__(self):
          print("EMPLOYEE  CLASS CREATED")
     def __del__(self):
          print("EMPLOYEE CLASS DESTRUCTED")
obj=employee()
del obj
