# Python Functions - Complete Guide

## Overview
This tutorial covers Python functions comprehensively through practical examples and problem-solving. Functions in Python are treated differently from other languages, with unique syntax and capabilities.

---

## 1. Basic Function Syntax

### Function Definition Structure
```python
def function_name(parameter):
    # Function body (indented)
    return value  # Optional
```

### Key Components:
- **`def`** - Short for "definition"
- **Function name** - Should be descriptive (e.g., `square_of_num`)
- **Parameters** - Placeholders for values (remember: P for Placeholder, P for Parameters)
- **Colon (`:`)** - Marks the start of function body
- **Indentation** - Critical for function body

### Example: Square Function
```python
def square_of_num(num):
    return num ** 2

# Usage
result = square_of_num(4)
print(result)  # Output: 16
```

### Important Notes:
- **Parameters vs Arguments**: Technically, these are parameters (placeholders), not arguments
- **Return vs Print**: Use `return` to make values reusable, `print` only displays output
- Functions without `return` return `None` by default

---

## 2. Function with Multiple Parameters

### Syntax
```python
def function_name(param1, param2, param3):
    return param1 + param2 + param3
```

### Example: Addition Function
```python
def add_two_nums(num1, num2):
    return num1 + num2

# Usage
result = add_two_nums(5, 5)
print(result)  # Output: 10
```

---

## 3. Polymorphism in Functions

**Polymorphism** = One thing, many tasks

Python's built-in operators naturally support polymorphism:

### Example: Multiply Function
```python
def multiply(p1, p2):
    return p1 * p2

# Works with numbers
print(multiply(8, 5))    # Output: 40

# Works with strings
print(multiply("h", 5))  # Output: hhhhh

# Mixed types
print(multiply(5, "a"))  # Output: aaaaa
```

---

## 4. Functions Returning Multiple Values

### Syntax
```python
def function_name(param):
    value1 = calculation1
    value2 = calculation2
    return value1, value2  # Returns as tuple
```

### Example: Circle Statistics
```python
import math

def circle_stats(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference

# Usage - Unpacking multiple return values
area, circumference = circle_stats(3)
print(f"Area: {area}")
print(f"Circumference: {circumference}")
```

### Key Points:
- Multiple values are returned as a tuple by default
- Can be unpacked into separate variables
- `return` statement immediately ends function execution

---

## 5. Default Parameter Values

### Syntax
```python
def function_name(param="default_value"):
    return f"Hello, {param}!"
```

### Example: Greeting Function
```python
def greet(name="user"):
    return f"Hello, {name}!"

# Usage
print(greet("Chai"))    # Output: Hello, Chai!
print(greet())          # Output: Hello, user!
```

### Benefits:
- Makes parameters optional
- Provides fallback behavior
- Reduces function call complexity

---

## 6. Lambda Functions (Anonymous Functions)

### Syntax
```python
variable_name = lambda parameters: expression
```

### Example: Cube Function
```python
# Traditional function
def cube_traditional(num):
    return num ** 3

# Lambda function
cube = lambda x: x ** 3

# Usage
print(cube(3))  # Output: 27
```

### Characteristics:
- **Anonymous** - No function name required
- **One-line** - Expression only, no statements
- **Inline** - Defined where needed
- **Limited scope** - Best for simple operations

### When to Use:
- Short, simple operations
- Framework callbacks (Django, Flask)
- Functional programming patterns

---

## 7. Variable Arguments (*args)

### Purpose
Handle functions that accept varying numbers of arguments.

### Syntax
```python
def function_name(*args):
    # args is a tuple containing all arguments
    return sum(args)  # Example operation
```

### Example: Sum All Function
```python
def sum_all(*args):
    return sum(args)

# Usage
print(sum_all(1, 2))           # Output: 3
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
print(sum_all(6, 7, 8, 9, 10, 11)) # Output: 51
```

### Key Points:
- **`*args`** - Standard naming convention (can be changed, but don't)
- **Tuple format** - Arguments stored as tuple
- **Iterable** - Can loop through with `for i in args:`
- **Asterisk required** - `*` tells Python to expect multiple arguments

### Manual Processing Example:
```python
def process_args(*args):
    for i in args:
        print(i * 2)  # Double each argument
    return sum(args)
```

---

## 8. Keyword Arguments (**kwargs)

### Purpose
Handle functions that accept any number of keyword (named) arguments.

### Syntax
```python
def function_name(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

### Example: Print Key-Value Pairs
```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Usage
print_kwargs(name='Shaktiman', power='laser')
print_kwargs(name='Shaktiman', power='laser', enemy='Dr. Jackaal')
```

### Key Points:
- **`**kwargs`** - Standard naming (keyword arguments)
- **Dictionary format** - Arguments stored as key-value pairs
- **Flexible calling** - Arguments can be passed in any order
- **`.items()`** - Required to iterate over key-value pairs

### Flexible Parameter Order:
```python
# These calls are equivalent:
print_kwargs(name='Alice', power='telepathy')
print_kwargs(power='telepathy', name='Alice')
```

---

## 9. Generator Functions (yield)

### Purpose
Create functions that generate values on-demand, preserving memory and state.

### Key Concept: Memory Perspective
- **`return`** - Ends function execution, returns value once
- **`yield`** - Pauses function, remembers state, can resume

### Example: Even Number Generator
```python
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

# Usage
for num in even_generator(10):
    print(num)  # Output: 2, 4, 6, 8, 10
```

### Why Use Generators?
- **Memory efficient** - Values generated on-demand
- **State preservation** - Function remembers where it left off
- **Lazy evaluation** - Values computed only when needed

### Comparison:
```python
# Regular function - returns all at once
def even_list(limit):
    return [i for i in range(2, limit + 1, 2)]

# Generator function - yields one at a time
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
```

---

## 10. Recursive Functions

### Concept
A function that calls itself to solve smaller versions of the same problem.

### Essential Components:
1. **Base case** - Exit condition to stop recursion
2. **Recursive case** - Function calls itself with modified parameters

### Example: Factorial Function
```python
def factorial(n):
    # Base case - exit strategy
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Usage
print(factorial(5))  # Output: 120
```

### How It Works:
```
factorial(5) = 5 * factorial(4)
factorial(4) = 4 * factorial(3)
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1 * factorial(0)
factorial(0) = 1  # Base case

# Then calculates back up:
# 1 * 1 = 1
# 2 * 1 = 2
# 3 * 2 = 6
# 4 * 6 = 24
# 5 * 24 = 120
```

### Recursion Strategy:
1. **Identify the pattern** - How does the problem break down?
2. **Define base case** - When should recursion stop?
3. **Implement recursive case** - How does function call itself?

---

## Summary of Key Concepts

### Function Fundamentals
- Use `def` to define functions
- Parameters are placeholders, use descriptive names
- `return` makes values reusable, `print` only displays
- Indentation is critical

### Advanced Features
- **Multiple parameters** - Separate with commas
- **Multiple return values** - Returned as tuples
- **Default parameters** - Provide fallback values
- **Lambda functions** - Anonymous, one-line functions

### Variable Arguments
- **`*args`** - Variable number of positional arguments (tuple)
- **`**kwargs`** - Variable number of keyword arguments (dictionary)

### Special Function Types
- **Generators** - Use `yield` for memory-efficient, stateful functions
- **Recursive** - Functions that call themselves (need base case)

### Best Practices
- Use descriptive function names
- Prefer `return` over `print` for reusability
- Include exit strategies for recursive functions
- Use appropriate argument types (*args, **kwargs) based on needs
- Test functions with different input types when using polymorphism

---

## Next Steps
- Practice writing functions with different parameter types
- Experiment with generators for large data sets
- Study recursion patterns in algorithms
- Learn about function decorators and advanced concepts