fruit = input("Enter Fruit: ")
color = input("Enter color: ")

if fruit.lower() == "banana":
    color = color.lower()
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("Overripe")
    else:
        print("Unknown banana color")
else:
    print("I don't have information about the fruit")