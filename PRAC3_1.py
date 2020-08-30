#PROGRAM TO PRINT FIBONACCI SERIES OF N NUMBERS USING CONCEPT OF COMMAND LINE ARGUMENTS, 
import sys
n = int(sys.argv[1])
def fibonnaci(n):
     n1, n2 = 0,1
     sum1,i=0,0
     while i < n:
          print(n1,end=" ")
          sum1=n1+n2
          n1=n2
          n2=sum1
          i+=1
fibonnaci(n)
