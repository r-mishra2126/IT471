from primefactor import is_prime as a

def main():
    num= int(input("Enter an integer:"))
    if a(num):
        print(num,"is prime")
    else:
        print(num, "not a prime")

main()
