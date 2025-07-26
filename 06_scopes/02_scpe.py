x = 99  # Global variable

def func2(y):
    z = x + y  # Can access global 'x'
    return z

result = func2(1)
print(result)  # Prints: 100