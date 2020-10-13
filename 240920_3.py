try:
     fh=open("testfile","w")
     try:
          fh.write("THIS IS MY TEST FILE FOR A EXCEPTION HANDLING")
          c=5/0
     except ZeroDivisionError as a:
          print(a)
     finally:
          print("GOING TO CLOSE THE FILE")
          fh.close()
except IOError:
     print("ERROR : CANNOT FIND THE FILE OR READ DATA")
