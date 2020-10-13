with open("hello.txt",'a') as demo:
    demo.write("v.v. nagar")

with open("hello.txt") as demo:
    print(demo.read())

with open("hello.txt") as demo:
    print(demo.readline())

with open("hello.txt") as demo:
    print(demo.readlines())
