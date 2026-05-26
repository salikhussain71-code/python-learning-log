#Day 2 column  version 

def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")

main()

#Day 2 Row version 

def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

# Day 3 size 

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

main()