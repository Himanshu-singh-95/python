# First Non-Repeated Character

input_string = input("Enter a string: ")

for char in input_string:
    print(f"Checking character: {char}")
    # Check if the character is non-repeated
    if input_string.count(char) == 1:
        print(f"The first non-repeated character is: {char}")
        break
else:
    print("No non-repeated character found.")