n=int(input("ENTER LIMIT:"))
for i in range(0,n):
      for k in range(n-i-2,-1,-1):
           print("  ",end="")
      for j in range(0,i*2+1):
           print("*",end="")
      for k in range(n-i-2,-1,-1):
           print("  ",end="")
      print("")
