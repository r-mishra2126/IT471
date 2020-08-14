def table(n):
    return lambda a:a*n;

n=int(input("Enter the number"))
b=table(n)
print(b(1))
for i in range(1,11):
    print (n,"X",i,"=",b(i));

    
