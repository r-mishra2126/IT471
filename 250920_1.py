def check(n):
     if n<5:
          raise("ENTER VALUE OF N GREATER THAN >5")
def function():
     try:
          n=eval(input("ENTER THE VALUE OF N: "))
          check(n)
     except ValueError as e:
          print("VALUE ERROR : ",e)
     else:
          print("VALUE OF N : ",n)
     finally:
          print("VALUE OF N IS PRINTED")
function()
          
       
