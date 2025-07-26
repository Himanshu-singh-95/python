# Problem Statement:
# "Check password strength based on character length."
# Requirements:

# Less than 6 characters → Weak
# 6 to 10 characters → Medium
# More than 10 characters → Strong


password = input("Enter your password: ").strip()

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print(f"Password strength is {strength}")