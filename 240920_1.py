try:
     fh=open("demo","r")
     print(fh.read())
except IOError:
     print("ERROR CANNOT FIND THE FILE")
else:
     print("READ SUFFESSFULLY")
     fh.close()
