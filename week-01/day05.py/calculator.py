def main():
    print("=== Day 05 Calculator ===")
    
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    
    print("\nResults:")
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}")
    print(f"{x} % {y} = {x % y}")

if __name__ == "__main__":
    main()