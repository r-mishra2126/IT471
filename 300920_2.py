class A:
     var=1
     def __init__(self):
          print(self.var,A.var)
          self.__class__.var+=2
          print(self.var,A.var)
          A.var+=2
          print(self.var,A.var)
          self.var+=2
          print(self.var,A.var)
          print(" " )

     def show(self):
          print(self.var,A.var)
x=A()
x.show()
print(" ")
y=A()
y.show()
x.show()
