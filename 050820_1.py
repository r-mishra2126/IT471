def add(x):
     def ad(y):
          return x + y
     def sub(z):
          return x - z
     return ad,sub
f,s = add(5)
print(f(5))
print(s(2))
