try:
    raise NameError('Hithere')
except NameError as e:
    print("an exception flew by",e)

