def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))

            if x <= 0:
                raise ValueError

            return x

        except ValueError:
            print("x must be a positive integer")


main()