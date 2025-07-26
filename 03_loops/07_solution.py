# Problem Statement:
# "Keep asking the user for input until they enter a number between 1 and 10."

# If the user enters a number outside this range, the program should prompt them again
# Keep taking input until they provide a valid number (between 1 and 10)

while True:
    number = int(input("Enter a number between 1 and 10: "))
    if 1 <= number <= 10:
        print(f"You entered a valid number: {number}")
        break
    else:
        print("Invalid number. Please try again.")
# This loop will continue until a valid number is entered.