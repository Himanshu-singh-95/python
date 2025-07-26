# Python Data Types - Complete Overview

## Introduction
This video provides a comprehensive overview of Python data types (also called object types). Understanding data types is crucial because programs need to store different kinds of data in memory and perform computations on them.

## Python Comments
```python
# This is a comment
# In VS Code, use Ctrl+/ for auto-comments
```

## Main Data Types in Python

### 1. Numbers
Numbers come in various forms:

#### Basic Numbers
```python
1, 2, 3, 4  # Integers
3.14        # Float (decimal numbers)
```

#### Complex Numbers
```python
3 + 4j      # Complex numbers (j represents imaginary unit)
```

#### Special Number Types
```python
Decimal()   # For precise decimal calculations
Fraction()  # For fraction representations
```

#### Number Operations
```python
12 + 12     # Basic arithmetic: 24
5.0         # Decimal operations
2 ** 4      # Power operation: 2^4 = 16
2 ** 100    # Python handles large numbers easily
```

#### Math Library
```python
import math
math.pi     # Access pi value
import random
random.random()           # Generate random number
random.choice([1,2,3,4,5]) # Random choice from list
```

### 2. Strings
Strings are sequences of characters and are **immutable**.

#### String Creation
```python
username = "chai aur code"    # Double quotes
'spam'                        # Single quotes
"Bob's"                       # Use double quotes for apostrophes
b'a\x01c'                     # Byte strings
u'unicode'                    # Unicode strings
```

#### String Operations
```python
len(username)     # Get string length
username[0]       # Access first character: 'c'
username[-1]      # Access last character: 'e'
username[1:3]     # Slicing: 'ha' (start:end, end not included)
```

#### Important Note
```python
# This will cause an error - strings are immutable!
username[0] = 'A'  # TypeError: 'str' object does not support item assignment
```

#### String Methods
```python
dir(username)  # See all available methods
# Returns: lstrip, isdecimal, format, count, etc.
```

### 3. Lists
Lists are **mutable** ordered collections that can store different data types.

#### List Creation
```python
my_list = [1, 23, "chai", 3.14]  # Mixed data types allowed
```

#### List Operations
```python
len(my_list)     # Get list length: 4
my_list[0]       # Access first element: 1
my_list[-1]      # Access last element: 3.14
my_list[1:3]     # Slicing works on lists too
```

#### Key Difference from Strings
- Lists are **mutable** - you can change individual elements
- Strings are **immutable** - you cannot change individual characters

### 4. Tuples
Tuples are **immutable** ordered collections, similar to lists but cannot be changed after creation.

#### Tuple Creation
```python
my_tup = (1, 2, 3, 4)  # Uses parentheses instead of square brackets
```

#### Tuple Operations
```python
len(my_tup)      # Get tuple length
my_tup[0]        # Access first element: 1
```

#### Lists vs Tuples
- **Lists**: Mutable, use square brackets `[]`
- **Tuples**: Immutable, use parentheses `()`

### 5. Dictionaries
Dictionaries store key-value pairs and use curly braces `{}`.

#### Dictionary Creation
```python
myD = {
    1: "lemon",
    2: "ginger", 
    "comic": "Nagraj"
}
```

#### Dictionary Operations
```python
myD["comic"]     # Access value by key: "Nagraj"
myD[1]           # Access by numeric key: "lemon"
# myD["nonexistent"]  # Would raise KeyError
```

#### Key Features
- No zero-based indexing like lists
- Access values using custom keys
- Keys can be strings, numbers, or other immutable types

### 6. Sets
Sets store only **unique values** (no duplicates allowed).

```python
# Example: {a, b, b, c} would become {a, b, c}
# Useful for mathematical operations and removing duplicates
```

### 7. Boolean
Simple True/False values.

```python
True
False
```

### 8. None Type
Represents "nothing" or empty value.

```python
None  # Used when no value is available (e.g., API returns no data)
```

## Advanced Data Types (Future Topics)

### Functions
- Custom functions for reusable code

### Modules
- Code organization and reusability

### Classes
- Object-oriented programming concepts
- Inheritance, methods, instantiation

### File Handling
- Reading and writing files
- Text files, CSV files, etc.

### Advanced Concepts
- **Decorators**: Enhance existing functionality
- **Generators**: Memory-efficient iterators  
- **Iterators**: Objects that can be iterated over
- **Comprehensions**: Concise way to create lists/dicts
- **Metaprogramming**: Code that manipulates code

## Important Programming Concepts

### Bracket Types
Remember the difference between:
- **Brackets**: `[]` - Used for lists
- **Parentheses**: `()` - Used for tuples and function calls
- **Braces/Curly Braces**: `{}` - Used for dictionaries and sets

### Mutable vs Immutable

#### Immutable Types
- Strings, tuples, numbers
- Cannot be changed after creation
- Operations create new objects

#### Mutable Types  
- Lists, dictionaries, sets
- Can be modified after creation
- Operations modify existing objects

### Getting Help in Python
```python
dir(object_name)  # See all available methods and attributes
help(object_name) # Get detailed help information
```

## Key Takeaways

1. **Data types are fundamental** - Master them first before moving to conditionals, loops, and functions
2. **Understand mutability** - Know which types can be changed and which cannot
3. **Practice indexing** - Most data types support indexing and slicing
4. **Use appropriate brackets** - Square `[]`, parentheses `()`, and curly braces `{}` have different meanings
5. **Python is flexible** - You can mix different data types in lists
6. **Error messages are helpful** - Read errors carefully (like KeyError for dictionaries)

## Next Steps
The upcoming videos will dive deep into each data type individually, covering:
- Detailed operations for each type
- Best practices and use cases
- Real-world applications
- Performance considerations

Once you master data types, everything else (conditionals, loops, functions) becomes much easier!