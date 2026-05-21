# Program 1 - While/For Loop
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")

# Program 2 - Functions with hardcoded value
def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")

main()

# Program 3 - Full refactored version
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()