#define python user-defined exceptions
class Error(Exception):
    """base class for other exception"""
    pass

class ValueTooSmallError(Error):
    """raised when the input is small"""
    pass

class ValueTooLargeError(Error):
    """raised when the input value is too large"""
    pass

#our main program
#user guesses a number until he/she gets it right
#you need to guess this number
number = 10

while True:
    try:
        i_num=int(input("enter the number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("value is too small,try again")
        print()
    except ValueTooLargeError:
        print("value is too small,try again")
        print()

print("congo u guessed it coreectly")
