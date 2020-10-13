def findfact(n):
    res=1
    for i in range(1,n+1):
        res=res*1
    return str(res)

f= open("dest.txt",'w')
f.write("my name is abc i  stay in anand")
f.seek(10,0)
f.write(findfact(5))
f.close()

f1=open("dest.txt",'r')
print(f1.read())
