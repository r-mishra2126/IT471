def spam(divideBy,z):
     try:
          x=42/divideBy
          y=int(z)
          return x,z
     except(ZeroDivisionError,ValueError) as x:
          print("ERROR: INVALID ARGUEMENT",x)
print(spam(2,3))
print(spam(12,'xyz'))
print(spam(0,3))
print(spam(1,3))
