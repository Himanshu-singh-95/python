# Python Scopes and Namespaces - Study Notes

## Introduction
Scopes and namespaces are fundamental concepts in Python that determine where variables can be accessed in your code. Understanding these concepts is crucial for writing reliable and maintainable Python programs.

## What are Scopes and Namespaces?

### Definition
- **Scope**: Defines where in your code a variable can be accessed
- **Namespace**: A container that holds variable names and their references
- Both concepts serve almost the same purpose and have the same fundamental foundation

### Key Analogy: The House Concept
Think of scopes like houses in memory:
- **Global scope** = The outside world
- **Function scope** = A house with its own space
- **Nested functions** = Rooms inside the house

## Scope Hierarchy in Python

### 1. Global Scope
```python
username = "chai aur code"  # Global variable
print(username)  # Accessible anywhere
```

### 2. Function Scope
```python
def func():
    username = "chai"  # Local variable (inside the house)
    print(username)   # Prints "chai"

func()
print(username)  # Still prints "chai aur code" (global unchanged)
```

### 3. Variable Lookup Rule
When Python looks for a variable, it follows this order:
1. **Local scope** (inside current function)
2. **Enclosing scope** (parent function)
3. **Global scope** (module level)
4. **Built-in scope** (Python built-ins)

## Practical Examples

### Example 1: Basic Scope Behavior
```python
username = "chai aur code"  # Global

def func():
    username = "chai"  # Local - doesn't affect global
    print(username)    # Prints: chai

func()
print(username)  # Prints: chai aur code
```

### Example 2: Accessing Global Variables
```python
x = 99  # Global variable

def func2(y):
    z = x + y  # Can access global 'x'
    return z

result = func2(1)
print(result)  # Prints: 100
```

### Example 3: Nested Function Scopes
```python
x = 99  # Global

def f1():
    x = 88  # Local to f1
    
    def func2():
        print(x)  # Accesses f1's local x (88), not global x (99)
    
    func2()

f1()  # Prints: 88
```

## The `global` Keyword

### What it does
The `global` keyword allows you to modify global variables from inside a function.

```python
x = 99  # Global

def func3():
    global x  # Tells Python to use the global x
    x = 12    # Modifies the global variable
    print(x)  # Prints: 12

func3()
print(x)  # Prints: 12 (global x was changed)
```

### ⚠️ Important Warning
**Avoid using `global` keyword in most cases!**

**Why?**
- Makes code unpredictable
- Hard to debug when multiple functions modify global variables
- Reduces code reliability
- Makes collaboration difficult

**Best Practice**: Access global variables for reading, but avoid modifying them.

## Key Rules and Concepts

### 1. Scope Creation
- Every function creates its own scope (namespace)
- Variables declared inside a function are local to that function
- Python uses **indentation** instead of curly braces to define scopes

### 2. Variable Shadowing
```python
name = "global"

def test():
    name = "local"  # Shadows the global variable
    print(name)     # Prints: local

test()
print(name)  # Prints: global (unchanged)
```

### 3. Scope Resolution
If a variable isn't found locally, Python searches:
- Enclosing function scopes
- Global scope
- Built-in scope
- If not found anywhere → `NameError`

## Common Patterns

### Reading Global Variables
```python
counter = 0  # Global

def increment():
    return counter + 1  # ✅ Good: Reading global

result = increment()
```

### Avoiding Global Modifications
```python
# ❌ Avoid this
def bad_function():
    global counter
    counter += 1

# ✅ Better approach
def good_function(current_value):
    return current_value + 1

counter = good_function(counter)
```

## Programming Tips

### 1. Understanding Variables
The most important skill in programming is knowing:
- What value is stored in each variable
- What data type each variable has
- This understanding transfers across all programming languages

### 2. Debugging Scope Issues
When facing scope-related errors:
1. Trace where the variable is declared
2. Check which scope you're trying to access it from
3. Verify the variable exists in the expected scope

### 3. Best Practices
- Keep global variables to a minimum
- Use function parameters instead of global variables
- Return values from functions rather than modifying globals
- Use descriptive variable names (avoid single letters like `x`, `y` in production code)

## Summary

Scopes and namespaces in Python work like houses and rooms:
- Each function is like a house with its own space
- Variables inside functions are private to that function
- Functions can access variables from outer scopes
- Avoid modifying global variables from inside functions
- Understanding variable scope is fundamental to mastering any programming language

Remember: If you understand what values your variables hold and their scope, you understand 90% of programming!