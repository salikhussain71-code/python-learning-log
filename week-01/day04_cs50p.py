def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)



def hello(to):
    print("hello,", to)

name = input("What's your name? ")
hello(name)



def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()


def main():
    x = int(input("What's x? "))
    print("Squared is", square(x))

def square(n):
    return n * n

main()