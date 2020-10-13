fo=open("hello.txt","r")
print("name of the file:", fo.name)

line = fo.readline()
print("REad line: %s" % (line))

p=fo.tell()

print("position of pointer is : %d" %p)
#again set the pointer to the begining
fo.seek(3,0)
linme=fo.readline()
print("REad line: %s" % (line))

#close opend file
fo.close()
