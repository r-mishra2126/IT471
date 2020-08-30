#PROGRAM TO FIND SUM OF ALL INTEGERS GREATER THAN 100 & LESS THAN 200 AND ARE DIVISIBLE BY 5.
sum_=0
for i in range(101,200):
     if i%5==0:
          sum_=sum_+i
print("SUM = ",sum_)
