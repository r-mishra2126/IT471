class first:
    def __init__(self):
        self.a=5
        self.b=6
    def display(self):
        print("a:",self.a)
        print("b:",self.b)

class second(first):
    def __init__(self):
        self.c=7
        self.d=8
    def display(self):
        print("c:",self.c)
        print("d:",self.d)

class multiply(first):
    def __init__(self):
        first.__init__(self):
            self.e=11
            self.f=12
    def mul(self):
        print(self.a)
        
        print("a:",self.a)
        print("b:",self.b)
