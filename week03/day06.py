# writing topic
name = input("What's your name? ")

with open("log.txt", "w") as file:
    file.write(name)

print("Saved!")


# line in file
with open("log.txt", "r") as file:
    for line in file:
        print(line)