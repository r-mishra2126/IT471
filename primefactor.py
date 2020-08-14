from math import sqrt

def is_prime(n):
    x = 2
    root = sqrt(n)
    while x <= root:
        if n % x==0:
            return False;
        x=x+1

    return True;
