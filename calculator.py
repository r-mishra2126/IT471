from cal import add,sub,mul,div

import cal
from 

a=eval(input("enter the value of a:"))
b=eval(input("enter the value of b:"))
print("enter ur choice for calculation")
print("1. addtion \n 2. subt \n 3. mult \n 4. div \n")

c=int(input("enter your choice"))

if(c==1):
    print("addition is",add(a,b))

elif(c==2):
    print("subt is",sub(a,b))

elif(c==3):
    print("mult is",mul(a,b))

elif(c==4):
    print("div is",div(a,b))

else:
    print("enter right ur choice")
