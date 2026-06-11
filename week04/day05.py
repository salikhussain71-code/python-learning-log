def main():
    name = get_name("What's your name? ")
    print(f"hello, {name}")


def get_name(prompt):
    while True:
        name = input(prompt)

        if name:
            return name


main()