import cowsay
import sys

name = sys.argv[1] if len(sys.argv) == 2 else "friend"
cowsay.cow(f"Day 3 done, {name}!")