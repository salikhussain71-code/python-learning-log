name = input("What did you study today? ")

with open("log.txt", "a") as file:
    file.write(name + "\n")

print("Saved to log!")