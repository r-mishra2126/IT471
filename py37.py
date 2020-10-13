class angle:
    d=1
    #def __init__(self,n)
    def abc(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def display(self):
        print(self.a, self.b,self.c,)
        print(self.d)

a=angle()
#a=angle(10,20,30)
#a.abc is removed
a.abc(10,20,30)
a.display()
print(dir(a))
