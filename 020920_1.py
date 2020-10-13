#READ AND WRITE TO A FILE
file1=open('ost.txt','w')
file1.write("OPEN SOURCE TECHNOLOGY ")
file1.close()
file2=open('ost.txt','r')
print(file2.read())
