class base:
    def __init__(self):
        self.a=5
        self.b=6
    def display(self):
        print(self.a)
        print(self.b)

class derived(base):
    def __init__(self):
        base.__init__(self)

    def show(self):
        print(self.a)
        print(self.b)

class multilevel(derived):
    def __init__(self):
        base.__init__(self)
        self.e=10
        self.f=20
    def display(self):
        print(self.a)
        print(self.b)
        print(self.e)
        print(self.f)

b= base()
b.display()
c=derived()
c.display()
c.show()
m=multilevel()
m.display()
