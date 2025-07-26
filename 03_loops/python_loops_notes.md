# Python Loops - Complete Tutorial Notes

## Introduction
- Loops in Python are treated differently from other programming languages
- Python has a unique way of handling loops (iterables/iterators) 
- Understanding Python's approach to loops is crucial for data science interviews
- This tutorial covers practical implementation before diving into internals

## Key Loop Concepts

### For Loops
- Basic syntax: `for variable in iterable:`
- The variable name can be anything (num, char, i, etc.)
- Indentation is crucial - defines what's inside the loop
- Python automatically provides proper indentation

### While Loops  
- Syntax: `while condition:`
- Continues as long as condition is True
- Useful when you don't know exact number of iterations
- Be careful to avoid infinite loops

### Important Keywords

#### `continue`
- Skips the current iteration and moves to the next one
- Used with conditional checks
- Example: Skip 5th iteration in a multiplication table

#### `break`
- Terminates the entire loop immediately
- Different from `continue` which only skips one iteration
- Useful for early exit when condition is met

## Practical Problems Solved

### 1. Counting Positive Numbers
```python
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1

print("Final count of positive numbers is", positive_number_count)
```

**Key Concepts:**
- Looping through lists
- Conditional checking with `if`
- Counter variables
- Descriptive variable naming (avoid abbreviations)

### 2. Sum of Even Numbers
```python
n = 10
sum_even = 0

for i in range(1, n + 1):
    if i % 2 == 0:  # Check if divisible by 2
        sum_even += i

print("Sum of even numbers is:", sum_even)
```

**Key Concepts:**
- `range()` function usage
- Modulus operator (%) for checking divisibility
- Range is exclusive of end value
- Increment operators (`+=`)

### 3. Multiplication Table with Skip
```python
number = 3

for i in range(1, 11):
    if i == 5:
        continue  # Skip 5th iteration
    print(f"{number} x {i} = {number * i}")
```

**Key Concepts:**
- Using `continue` to skip iterations
- String formatting in print statements
- Conditional detection within loops

### 4. Reverse String Using Loop
```python
input_string = "python"
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string

print(reversed_string)
```

**Key Concepts:**
- String manipulation character by character
- String concatenation
- Strings are immutable in Python
- Always follow requirements first, optimization second

### 5. First Non-Repeated Character
```python
input_string = "teeter"

for char in input_string:
    if input_string.count(char) == 1:
        print("The character is", char)
        break  # Exit after finding first occurrence
```

**Key Concepts:**
- `.count()` method for strings
- Early termination with `break`
- Optimization: stop when result is found

### 6. Factorial Using While Loop
```python
number = 5
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1
    # Can be shortened to: factorial *= number; number -= 1

print("Factorial value is", factorial)
```

**Key Concepts:**
- While loop syntax and conditions
- Avoiding infinite loops
- Compound assignment operators (`*=`, `-=`)
- Starting with appropriate initial values

### 7. Input Validation
```python
while True:
    number = int(input("Enter a value between 1 and 10: "))
    
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number. Try again.")
```

**Key Concepts:**
- Infinite loop with `while True`
- Input validation and conversion
- Python's chained comparison operators (`1 <= number <= 10`)
- User input handling

### 8. Prime Number Checker
```python
number = 29
is_prime = True

if number > 1:
    for i in range(2, number):
        remainder = number % i
        if remainder == 0:
            is_prime = False
            break

print(is_prime)
```

**Key Concepts:**
- Boolean variables and assumptions
- Mathematical logic implementation
- Breaking complex conditions into steps
- Range optimization (don't need to check up to the number itself)

### 9. List Uniqueness Checker
```python
items = ["apple", "banana", "orange", "apple", "banana"]
unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate", item)
        break
    else:
        unique_items.add(item)
```

**Key Concepts:**
- Sets for unique value storage
- Membership testing (`in` operator)
- Set methods (`.add()`)
- Early duplicate detection

### 10. Exponential Backoff Strategy
```python
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(f"Attempt {attempts + 1}, Wait Time {wait_time}")
    time.sleep(wait_time)
    wait_time *= 2  # Double the wait time
    attempts += 1
```

**Key Concepts:**
- Importing modules (`time`)
- Real-world application example
- Exponential growth patterns
- System sleep functionality

## Important Programming Principles

### 1. Readability First
- Use descriptive variable names
- Don't abbreviate unnecessarily
- Code should read like English

### 2. Requirements First, Optimization Second
- Always implement what's asked first
- Optimize later if needed
- Don't over-engineer initially

### 3. Indentation is Everything
- Python uses indentation to define code blocks
- Consistent indentation is crucial
- Each level of indentation represents nesting

### 4. Problem-Solving Approach
- Break down complex problems into smaller steps
- Write step-by-step logic on paper first
- Test with simple examples
- Don't be afraid to print intermediate values for debugging

## Python-Specific Features

### Range Function
- `range(start, stop, step)`
- `range(10)` - 0 to 9
- `range(1, 11)` - 1 to 10
- Always exclusive of the end value

### String Methods
- `.count(substring)` - counts occurrences
- Strings are iterable (can loop through characters)
- String concatenation creates new strings (immutable)

### Chained Comparisons
- `1 <= x <= 10` instead of `x >= 1 and x <= 10`
- More readable and Pythonic

### Sets
- Automatically maintain unique elements
- Fast membership testing
- Useful for duplicate detection

## Best Practices

1. **Variable Naming**: Use clear, descriptive names
2. **Comments**: Explain the logic, not the syntax
3. **Testing**: Verify your logic with simple examples
4. **Error Handling**: Consider edge cases
5. **Code Structure**: Keep it simple and readable

## Next Steps
- Practice these 10 problems multiple times
- Try variations of each problem
- Next video will cover the internal workings of Python loops and iterators
- Understanding internals will help with advanced Python programming

## Summary
This tutorial covered practical loop implementation in Python through 10 hands-on problems. The focus was on understanding syntax, control flow, and problem-solving approaches rather than diving into complex theory. The next lesson will explore how Python handles loops internally, which is crucial for advanced Python programming and technical interviews.