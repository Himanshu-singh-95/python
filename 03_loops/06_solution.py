# Factorial Using While Loop
number = int(input("Enter a number to calculate its factorial: "))
factorial = 1

while number > 0: 
    factorial *= number
    number -= 1
print(f"Factorial: {factorial}")