def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if _name_ == "_main_":
    main()


import sys
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
