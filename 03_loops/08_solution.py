# Prime Number Checker
input_number = int(input("Enter a number to check if it's prime: "))
is_prime = True

if input_number > 1:
    for i in range(2, input_number):
        if (input_number % i) == 0:
            is_prime = False
            break

if is_prime:
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")