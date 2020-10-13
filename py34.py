class CustomError(Exception):
    pass

try:
    raise Customerror("can u reach me?")
except CustomError as e:
    print("Cathced CustomError: {}".format(e))
except Exception as e:
    print ("Generic exception: {}".format(e))
