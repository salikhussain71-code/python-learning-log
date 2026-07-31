import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex(f"hello, {sys.argv[1]}")
