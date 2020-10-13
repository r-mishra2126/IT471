fo = open("hello.txt","r+")
print("NAMe of the file:", fo.name)

for index in range(5):
    try:
        line=next(fo)
        print("Line no %d - %s" % (index,line))
    except StopIteration:
        break

#close opend file
fo.close()
