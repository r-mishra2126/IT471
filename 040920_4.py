fo=open("HELLO.TXT","r+")
print("NAEM OF TE FILE",fo.name)
for index in range(5):
     try:
          line=next(fo)
          print("LINE NO %d - %s" %(index,line))
     except StopIteration:
          break
fo.close()
