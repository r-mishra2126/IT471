#CONTINUE
def continue_func( s):
     for i in range(len(s)):
          if i==5:
               print(" ",end="")
               continue
          print(s[i],end="")
     print("\n")
'''--------------------------------------------'''
#PASS
def pass_func(s):
     for i in range(len(s)):
          if i==5:
               print(" ",end="")
               pass
          print(s[i],end="")
     print("\n")
'''--------------------------------------------'''
#BREAK
def break_func(s):
     for i in range(len(s)):
          if i==5:
               print(" ",end="")
               break
          print(s[i],end="")
     print("\n")
'''--------------------------------------------'''
s="ABANDONED"
print("ORIGINAL STRING:",s)
print("STRING AFTER CONTINUE:")
continue_func( s)
print("STRING AFTER PASS:")
pass_func(s)
print("STRING AFTER BREAK:")
break_func(s)
