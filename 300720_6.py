n=int(input("ENTER THE NUMBER"))
factor=1
while factor <= n:
     if n % factor == 0:
          print(factor, end=' ',sep=" ")
     factor +=1
