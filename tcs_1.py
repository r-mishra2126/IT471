nop1=int(input("Enter number of pages of first book:"))
nol1=int(input("Enter number of lines per page of first book:"))
nop2=int(input("Enter number of pages(<1000) of second book:"))
nol2=int(input("Enter number of lines per page(<100) of second book:"))
read=int(input("Enter reading speed(in lines/seconds) of first book:"))
write=int(input("Enter writing speed  of second book:"))
time=int(input("enter time at which result is to be processed"))

nol_1=nol1
nop_1=nop1
total=nol_1*nop_1
n1=total/read

if (n1 >= time):
    time1=read*time
    page1=time1/nol1
    print("READ %d %d",page1, nol1)

elif(n1 < time):
    n2=time-n1
    lines2=write*n2
    page2=lines2/write
    print("WRITE page2 nol2",page2,nol2)

else:
    print("wrong inputs")
