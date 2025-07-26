# Multiplication Table with Skip 5th iteration

number = int(input("Enter a number to generate its multiplication table: "))

for i in range(1, 11):
    if i == 5:
        continue  # Skip the 5th iteration
    print(f"{number} x {i} = {number * i}")