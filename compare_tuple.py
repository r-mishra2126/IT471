tuple1 = ('python', 'geek') 
tuple2 = ('coder', 1) 
  
if (cmp(tuple1, tuple2) != 0): 
  
    # cmp() returns 0 if matched, 1 when not tuple1  
    # is longer and -1 when tuple1 is shoter 
    print('Not the same') 
else: 
    print('Same')
