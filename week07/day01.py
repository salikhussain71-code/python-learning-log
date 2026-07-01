import cowsay
import sys

if len(sys.argv) == 2:
  cowsay.cow(f"hllo,{sys.argv[1]}")
