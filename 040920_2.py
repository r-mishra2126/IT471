fo=open("hello.txt","r")
print("NAME OF FILE: ",fo.name)

line=fo.readline()
print("READ LINE: %s" %(line))
p=fo.tell()
print("POSITION OF POINTER IS: %d"%p)
print("----------------------------------------")
fo.seek(0,0)
g=fo.tell()
print("POSITION OF POINTER IS: ",g)
