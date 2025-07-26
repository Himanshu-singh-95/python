# Python Conditionals - Problem-Based Learning Notes

## Overview
This lesson covers Python conditionals through practical problem-solving rather than theoretical syntax. The approach focuses on learning by doing, solving 10 real-world problems using if-else statements.

## Key Concepts Covered

### 1. Taking User Input
```python
# Basic input syntax
user_score = input("Give me a score value: ")

# Converting input to integer (IMPORTANT!)
user_score_in_int = int(user_score)

# Or do it in one line
age = int(input("Provide me an age: "))
```

**Important Note**: All user input comes as strings by default and must be converted to appropriate data types.

### 2. Basic Conditional Syntax

#### If-Elif-Else Structure
```python
if condition1:
    # code block (note the indentation!)
    print("Condition 1 is true")
elif condition2:
    # another code block
    print("Condition 2 is true")
else:
    # default case
    print("None of the conditions were true")
```

#### Key Points:
- **Indentation is crucial** - Python uses indentation to define code blocks
- Use 4 spaces or consistent tabs
- Colon `:` is required after each condition
- `elif` is short for "else if"

### 3. Comparison Operators
- `<` : Less than
- `<=` : Less than or equal to
- `>` : Greater than  
- `>=` : Greater than or equal to
- `==` : Equal to (comparison)
- `!=` : Not equal to
- `=` : Assignment (single equals)

### 4. Advanced Conditional Techniques

#### Ternary Operator (Inline If-Else)
```python
# Syntax: value_if_true if condition else value_if_false
price = 12 if age >= 18 else 8
```

#### Logical Operators
```python
# AND - both conditions must be true
if (year % 4 == 0) and (year % 100 != 0):
    print("Leap year")

# OR - at least one condition must be true  
if condition1 or condition2:
    print("At least one is true")
```

#### Complex Conditions with Parentheses
```python
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print("Leap year")
```

### 5. Modulo Operator (%)
```python
# Check if divisible (remainder is 0)
if year % 4 == 0:
    print("Divisible by 4")

# Check if not divisible (remainder is not 0)
if year % 100 != 0:
    print("Not divisible by 100")
```

### 6. String Operations in Conditionals
```python
# String comparison (case-sensitive)
if weather == 'sunny':
    activity = "Go for a walk"

# Note: Consider case sensitivity
# 'Sunny' != 'sunny'
```

### 7. Variable Assignment Shortcuts
```python
# Long form
price = price - 2

# Short form (equivalent)
price -= 2
```

## Problem Solutions Walkthrough

### Problem 1: Age Group Categorization
```python
age = 25

if age < 13:
    print("Child")
elif age < 20:  # covers 13-19
    print("Teenager") 
elif age < 60:  # covers 20-59
    print("Adult")
else:           # 60+
    print("Senior")
```

### Problem 2: Movie Ticket Pricing
```python
age = 22
day = "Wednesday"

# Determine base price
price = 12 if age >= 18 else 8

# Apply Wednesday discount
if day == "Wednesday":
    price -= 2

print(f"Ticket price for you is ${price}")
```

### Problem 3: Grade Calculator with Validation
```python
score = 85

# Input validation
if score > 100:
    print("Please verify your grade again")
    exit()  # Exit program for invalid input

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Grade: {grade}")
```

### Problem 4: Fruit Ripeness Checker
```python
fruit = "banana"
color = "yellow"

if fruit == "banana":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("Overripe")
else:
    print("I don't have information about that fruit")
```

### Problem 9: Leap Year Checker (Complex Logic)
```python
year = 2024

# Leap year rules:
# 1. Divisible by 4 AND not by 100, OR
# 2. Divisible by 400
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

## Important Programming Concepts

### 1. Code Organization
- Keep conditions in logical order
- Use meaningful variable names
- Add comments for complex logic

### 2. Input Validation
```python
# Always validate user input
if score > 100:
    print("Invalid score")
    exit()
```

### 3. String Formatting
```python
# Modern f-string formatting (recommended)
print(f"Your grade is {grade}")

# Older methods
print("Your grade is", grade)
print("Your grade is {}".format(grade))
```

### 4. Error Handling Considerations
- Check for invalid inputs
- Use `exit()` to terminate program when needed
- Consider case sensitivity in string comparisons

## Best Practices Learned

1. **Start Simple**: Begin with basic conditions, add complexity gradually
2. **Use Proper Indentation**: Consistent 4-space indentation
3. **Validate Input**: Always check if user input is valid
4. **Meaningful Variables**: Use descriptive variable names
5. **Test Edge Cases**: Test boundary values (like exactly 18, 60, etc.)
6. **Comment Complex Logic**: Especially for conditions like leap year calculation

## Common Pitfalls to Avoid

1. **Using `=` instead of `==`** for comparisons
2. **Inconsistent indentation** - Python is very strict about this
3. **Forgetting to convert input types** - input() always returns strings
4. **Case sensitivity issues** with string comparisons
5. **Not handling edge cases** in range-based conditions

## Next Steps
- Practice with the remaining problems (Pet Food Recommendation)
- Try modifying existing solutions
- Experiment with taking user input instead of hardcoded values
- Practice combining multiple conditions with `and`/`or`

## Assignment
Complete the Pet Food Recommendation problem:
- Dog: < 2 years → puppy food, ≥ 2 years → adult food  
- Cat: > 5 years → senior cat food, ≤ 5 years → junior cat food

---
*Remember: The best way to learn programming is by solving problems, not just memorizing syntax!*