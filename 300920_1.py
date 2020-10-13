class angle:
     __d=1
     def inp(self,a,b,c):
          self.a=a
          self.b=b
          self.c=c

     def display(self):
          print(self.a,self.b,self.c)
a=angle()

a.inp(10,20,30)
a.display()
print(a.d)          
