class customerror(RuntimeError):
     def __init__(self,arg):
          self.arg=arg

try:
     a=eval(input("ENTER STRING"))
     b=eval(input("ENTER STRING 2 "))
     if type(a)!=str or type(b) !=str:
          raise customerror("INVALD ")
except customerror as e:
     print(e.arg)
else:
     c=a+b
     print(c)
