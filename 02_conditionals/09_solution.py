# Problem Statement:
# "Determine if a given year is a leap year."
# Leap Year Rules:

# Divisible by 4 AND not by 100, OR
# Divisible by 400

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
elif (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")