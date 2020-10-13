#READ AND WRITE TO A BINARY FILE.
f=open("binfile.bin","wb")
num=[5,10,15,20,25,26]
arr=bytearray(num)
print(arr)
f.write(arr)
f.close()

f=open("binfile.bin","rb")
num=list(f.read())
print(num)
f.close()
