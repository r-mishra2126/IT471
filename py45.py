class first:
    a=5
    def __init__(self):
        self.a=5
        self.b=6
    def display(self):
        print("a:",self.a)
        print("b:",self.b)

class second:
    b=6
    def __init__(self):
        self.c=7
        self.d=8
    def display(self):
        print("c:",self.c)
        print("d:",self.d)

class multiply(second,first):
    
    def mul(self):
        first.display(self)
    def add(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)
        second.display(self)

f1=first()
f1.display()
s1=second()
s1.display()
m1=multiply()
m1.mul()
m1.add()
