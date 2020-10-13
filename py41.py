class A:
    var=1

    def printvar(self):
        self.xxx()
        print("self.x=%d" % self.x)
        print("self.var is %d" % self.var)
        print("A.var is %d" % A.var)

    def xxx(self):
        self.x=A.var
        A.var+=1

    @staticmethod
    def MyStaticMethod():
        A.var+=1

a=A()
a.var = 2
a.printvar()
print("\n")
A.var = 3
a.printvar()
b=A()
A.MyStaticMethod()
b.printvar()
print(b.__dict__)
