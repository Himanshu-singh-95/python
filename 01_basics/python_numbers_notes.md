# Python Numbers - Complete Study Notes

## 📚 Overview
Python's number system is powerful and versatile, making it excellent for data science and scientific computing. When combined with libraries like NumPy, Python rivals MATLAB in numerical capabilities.

---

## 🔢 Core Number Types

### 1. **Integers and Floats**
- **Integers**: Whole numbers (`2`, `3`, `4`)
- **Floats**: Decimal numbers (`2.23`, `3.14`)
- Python handles mixed-type operations automatically

### 2. **Booleans**
- `True` and `False` (capital letters required)
- **Internally**: `True = 1`, `False = 0`
- Classified as numbers in Python

### 3. **Sets**
- Mathematical sets using `{1, 2, 3, 4}`
- Support mathematical operations

---

## ➕ Basic Arithmetic Operations

```python
x, y, z = 2, 3, 4

# Basic operations
x + y        # Addition: 5
x - y        # Subtraction: -1
x * y        # Multiplication: 6
x / y        # Division: 0.6667
x // y       # Floor division: 0
x % y        # Remainder: 2
x ** y       # Power: 8
```

---

## ✅ Best Practices

### 🚫 Code Clarity - Avoid:
```python
x + y * z    # Unclear precedence
40 + 2.23    # Mixed types without explicit conversion
```

### ✅ Prefer:
```python
(x + y) * z           # Clear with parentheses
float(40) + 2.23      # Explicit type conversion
int(2.23) + 40        # Explicit conversion
```

### 🎯 Key Principles
1. **Use parentheses** to clarify operation order
2. **Be explicit** about type conversions
3. **Maintain type consistency** in production code

---

## 🔍 Comparison and Logical Operations

### Comparison Operators
```python
1 < 2          # True
5.0 == 5.0     # True (equality)
4.0 != 5.0     # True (not equal)
1 <= 2         # True (less than or equal)
```

### Logical Operators
- **`and`**: Both conditions must be `True`
- **`or`**: At least one condition must be `True`

```python
x < y and y < z    # Both must be true
x < y or y > z     # Either can be true
```

---

## 🚀 Advanced Number Handling

### 📐 Math Library
```python
import math

# Floor and truncation
math.floor(3.5)    # 3 (always rounds down)
math.floor(-3.5)   # -4 (toward negative infinity)
math.trunc(2.8)    # 2 (toward zero)
math.trunc(-2.8)   # -2 (toward zero)
```

### 🔢 Number Base Systems
```python
# Different bases
0o20        # Octal (base 8) = 16 decimal
0xFF        # Hexadecimal (base 16) = 255 decimal
0b1000      # Binary (base 2) = 8 decimal

# Base conversions
oct(64)       # '0o100'
hex(64)       # '0x40'
bin(64)       # '0b1000000'
int('64', 8)  # Convert from base 8 to decimal
```

### 🎯 Precision Handling

#### ⚠️ Floating Point Issues
```python
# Problem
0.1 + 0.1 + 0.1 - 0.3  # Not exactly 0.0 due to precision

# Solution: Decimal module
from decimal import Decimal
result = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Result: exactly 0.0
```

#### 🧮 Fractions
```python
from fractions import Fraction
my_fraction = Fraction(2, 7)  # Represents 2/7 exactly
```

---

## 🎲 Random Number Generation

```python
import random

# Random integers
random.randint(1, 100)    # Random number from 1 to 99 (inclusive)

# Random choices
tea_options = ['lemon tea', 'masala chai', 'ginger tea', 'mint tea']
random.choice(tea_options)  # Returns random selection

# Shuffling
random.shuffle(tea_options)  # Modifies list in place
```

---

## 🔗 Set Operations

```python
set1 = {1, 2, 3, 4}
set2 = {1, 3, 5, 7}

# Mathematical operations
set1 & set2        # Intersection: {1, 3}
set1 | set2        # Union: {1, 2, 3, 4, 5, 7}
set1 - set2        # Difference: {2, 4}

# Important: Empty set
empty_set = set()  # Correct (not {})
type({})          # <class 'dict'> - this is a dictionary!
```

---

## ⭐ Special Features

### 🏗️ Large Number Handling
```python
# Python handles arbitrarily large integers
2 ** 100    # Works perfectly, unlike many languages
100 ** 2    # No overflow issues
```

### 🔤 Complex Numbers
```python
complex_num = 2 + 1j    # j represents imaginary unit
result = complex_num * 3  # (6+3j)
```

### 🔧 Bitwise Operations
```python
x = 1
x << 2     # Left shift: 1 becomes 4
x | 2      # Bitwise OR
x & 2      # Bitwise AND
```

---

## 📖 Essential Functions Reference

### 🔄 Type Conversion
- `int()` - Convert to integer
- `float()` - Convert to float
- `str()` - Convert to string

### ℹ️ Information Functions
- `type()` - Check data type
- `repr()` - Developer representation
- `print()` - User-friendly output

### 🧮 Mathematical Functions
- **Basic**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison**: `<`, `>`, `<=`, `>=`, `==`, `!=`
- **Logical**: `and`, `or`, `not`

---

## ⚠️ Common Pitfalls to Avoid

1. **Don't rely on operator precedence** - use parentheses
2. **Be careful with floating-point precision** - use Decimal when needed
3. **Empty sets vs empty dictionaries** - use `set()` not `{}`
4. **Type mixing** - be explicit about conversions
5. **Chained comparisons** - while possible, can be confusing

---

## 🎯 Practice Exercises

1. **Calculate compound interest** using proper type handling
2. **Create a number guessing game** using random
3. **Implement set operations** for student/teacher lists
4. **Handle decimal precision** in financial calculations
5. **Convert between different number bases**

---

## 🎓 Key Takeaways

- ✅ **Python excels at numerical computing**
- ✅ **Always prioritize code readability** and explicit intentions
- ✅ **Use appropriate libraries** for specialized numerical needs
- ✅ **Understand the difference** between floor, truncation, and rounding
- ✅ **Master set operations** for data manipulation
- ✅ **Handle precision issues** proactively in critical applications

---

> **💡 Note**: This foundation will prepare you for advanced topics in data science, scientific computing, and general Python programming!

---

## 📚 Additional Resources

- [Python Official Documentation - Numbers](https://docs.python.org/3/library/numeric.html)
- [Math Module Documentation](https://docs.python.org/3/library/math.html)
- [Decimal Module for Precision](https://docs.python.org/3/library/decimal.html)
- [Random Module Documentation](https://docs.python.org/3/library/random.html)