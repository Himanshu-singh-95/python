# Variable Arguments (*args)

def sum_all(*args):
    print(f"Arguments received: {args}")
    total = 0
    for num in args:
        total += num
    return total

# Usage
print(sum_all(1, 2))           # Output: 3
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
print(sum_all(6, 7, 8, 9, 10, 11)) # Output: 51