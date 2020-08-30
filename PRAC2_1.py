#PROGRAM TO PRINT THE LARGEST NUMBER AMONG THREE
max=0
num1=int(input("ENTER NUMBER 1:"))
num2=int(input("ENTER NUMBER 2:"))
num3=int(input("ENTER NUMBER 3:"))
if num1>num2:
     if num1>num3:
          max=num1
     else:
          max=num3
else:
     if num2>num3:
           max=num2
     else:
          max=num3
print("THE LARGEST NUMBER IS ",max)
