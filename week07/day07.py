import sys
import cowsay

# Check if at least one name was provided as an argument
if len(sys.argv) > 1:
    # Use sys.argv[1:] to loop through all names provided after the script name
    for name in sys.argv[1:]:
        cowsay.trex("hello, " + name)
else:
    cowsay.trex("hello, world")
