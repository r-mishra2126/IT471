class A:
    var=1
    def __init__(self):
        print(self.var, A.var)
        self.__class__.var+=2
        print(self.var, A.var)
        A.var+=2
        print(self.var, A.var)
        self.var+=2
        print(self.var, A.var)
        print("\n")

    def show(self):
        print (self.var, A.var)

x=A()
x.show()
print("\n")
y=A()
y.show()
x.show()
