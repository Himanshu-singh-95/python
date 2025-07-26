# Python Lists - Complete Study Notes

## Table of Contents
- [Introduction](#introduction)
- [Creating Lists](#creating-lists)
- [Accessing List Elements](#accessing-list-elements)
- [Modifying Lists](#modifying-lists)
- [Essential List Methods](#essential-list-methods)
- [Copying Lists](#copying-lists)
- [Basic Loops with Lists](#basic-loops-with-lists)
- [Conditional Statements](#conditional-statements)
- [Advanced Concepts](#advanced-concepts)
- [Key Takeaways](#key-takeaways)
- [Practice Exercises](#practice-exercises)

---

## Introduction

**Lists** are fundamental data structures in Python that store multiple values in a single variable. In other programming languages, they're often called arrays, but the Python community prefers the term "list."

### Key Characteristics:
- **Mutable**: Can be changed after creation
- **Ordered**: Elements have a defined order
- **Allow duplicates**: Same value can appear multiple times
- **Zero-indexed**: First element is at position 0

---

## Creating Lists

### Basic Syntax
Lists are created using square brackets `[]`:

```python
# Empty list
empty_list = []

# List with tea varieties
tea_varieties = ["Black Tea", "Green Tea", "Oolong Tea", "White Tea"]

# Mixed data types (possible but not recommended)
mixed_list = ["Tea", 42, True, 3.14]
```

### Best Practices
- Use descriptive variable names
- Keep similar data types together
- Use square brackets consistently

---

## Accessing List Elements

### Basic Indexing

#### Positive Indexing
```python
tea_varieties = ["Black Tea", "Green Tea", "Oolong Tea", "White Tea"]

print(tea_varieties[0])  # Output: "Black Tea"
print(tea_varieties[1])  # Output: "Green Tea"
print(tea_varieties[2])  # Output: "Oolong Tea"
print(tea_varieties[3])  # Output: "White Tea"
```

#### Negative Indexing
```python
print(tea_varieties[-1])  # Output: "White Tea" (last element)
print(tea_varieties[-2])  # Output: "Oolong Tea" (second to last)
```

### Slicing and Dicing

#### Slice Syntax: `list[start:end:step]`
- `start`: Starting index (inclusive)
- `end`: Ending index (exclusive)
- `step`: Step size (optional)

```python
tea_varieties = ["Black Tea", "Green Tea", "Oolong Tea", "White Tea"]

# Basic slicing
print(tea_varieties[0:2])   # Output: ["Black Tea", "Green Tea"]
print(tea_varieties[1:3])   # Output: ["Green Tea", "Oolong Tea"]

# Omitting start or end
print(tea_varieties[:2])    # Output: ["Black Tea", "Green Tea"]
print(tea_varieties[2:])    # Output: ["Oolong Tea", "White Tea"]

# Using step
print(tea_varieties[::2])   # Output: ["Black Tea", "Oolong Tea"]
```

#### Common Slicing Patterns
```python
# Get all elements
all_elements = tea_varieties[:]

# Reverse the list
reversed_list = tea_varieties[::-1]

# Get every second element
every_second = tea_varieties[::2]
```

---

## Modifying Lists

### Changing Individual Elements
```python
tea_varieties = ["Black Tea", "Green Tea", "Oolong Tea", "White Tea"]

# Change single element
tea_varieties[3] = "Herbal Tea"
print(tea_varieties)  # Output: ["Black Tea", "Green Tea", "Oolong Tea", "Herbal Tea"]
```

### Using Slicing for Multiple Changes

#### Replace Multiple Elements
```python
# Replace elements at positions 1 and 2
tea_varieties[1:3] = ["Green Tea", "Masala Chai"]
print(tea_varieties)  # Output: ["Black Tea", "Green Tea", "Masala Chai", "White Tea"]
```

#### Important Gotcha with String Assignment
```python
# ⚠️ This will insert each character separately
tea_varieties[1:2] = "Lemon"
print(tea_varieties)  # Output: ["Black Tea", "L", "e", "m", "o", "n", "Oolong Tea", "White Tea"]

# ✅ Correct way - wrap in list
tea_varieties[1:2] = ["Lemon Tea"]
print(tea_varieties)  # Output: ["Black Tea", "Lemon Tea", "Oolong Tea", "White Tea"]
```

#### Insert Without Replacing
```python
# Insert at position 1 without replacing
tea_varieties[1:1] = ["Earl Grey"]
print(tea_varieties)  # Inserts "Earl Grey" at position 1
```

#### Delete Elements Using Slicing
```python
# Delete elements by assigning empty list
tea_varieties[1:3] = []
print(tea_varieties)  # Removes elements at positions 1 and 2
```

---

## Essential List Methods

### Adding Elements

#### `.append(item)` - Add to End
```python
tea_varieties = ["Black Tea", "Green Tea"]
tea_varieties.append("Oolong Tea")
print(tea_varieties)  # Output: ["Black Tea", "Green Tea", "Oolong Tea"]
```

#### `.insert(index, item)` - Insert at Specific Position
```python
tea_varieties = ["Black Tea", "Oolong Tea", "White Tea"]
tea_varieties.insert(1, "Green Tea")  # Insert at index 1
print(tea_varieties)  # Output: ["Black Tea", "Green Tea", "Oolong Tea", "White Tea"]
```

### Removing Elements

#### `.pop()` - Remove and Return Last Element
```python
tea_varieties = ["Black Tea", "Green Tea", "Oolong Tea"]
removed_tea = tea_varieties.pop()
print(removed_tea)      # Output: "Oolong Tea"
print(tea_varieties)    # Output: ["Black Tea", "Green Tea"]
```

#### `.pop(index)` - Remove and Return Element at Index
```python
tea_varieties = ["Black Tea", "Green Tea", "Oolong Tea"]
removed_tea = tea_varieties.pop(1)
print(removed_tea)      # Output: "Green Tea"
print(tea_varieties)    # Output: ["Black Tea", "Oolong Tea"]
```

#### `.remove(item)` - Remove First Occurrence
```python
tea_varieties = ["Black Tea", "Green Tea", "Black Tea"]
tea_varieties.remove("Black Tea")  # Removes first occurrence
print(tea_varieties)  # Output: ["Green Tea", "Black Tea"]
```

### Other Useful Methods

```python
tea_varieties = ["Black Tea", "Green Tea", "Oolong Tea"]

# Get length
length = len(tea_varieties)  # Returns: 3

# Count occurrences
count = tea_varieties.count("Black Tea")  # Returns: 1

# Find index of element
index = tea_varieties.index("Green Tea")  # Returns: 1

# Sort the list
tea_varieties.sort()  # Sorts in place

# Reverse the list
tea_varieties.reverse()  # Reverses in place

# Clear all elements
tea_varieties.clear()  # Empties the list
```

---

## Copying Lists

### Understanding References vs Copies

#### Reference (Shallow Assignment)
```python
original = ["Black Tea", "Green Tea"]
reference = original  # Both variables point to the same list

reference.append("Oolong Tea")
print(original)   # Output: ["Black Tea", "Green Tea", "Oolong Tea"]
print(reference)  # Output: ["Black Tea", "Green Tea", "Oolong Tea"]
```

#### Creating a Copy
```python
original = ["Black Tea", "Green Tea"]
copy = original.copy()  # Creates a new list in memory

copy.append("Oolong Tea")
print(original)  # Output: ["Black Tea", "Green Tea"]
print(copy)      # Output: ["Black Tea", "Green Tea", "Oolong Tea"]
```

#### Alternative Copy Methods
```python
original = ["Black Tea", "Green Tea"]

# Method 1: .copy()
copy1 = original.copy()

# Method 2: list() constructor
copy2 = list(original)

# Method 3: Slicing
copy3 = original[:]
```

---

## Basic Loops with Lists

### For Loop - Iterating Through Elements
```python
tea_varieties = ["Black Tea", "Green Tea", "Oolong Tea"]

# Basic iteration
for tea in tea_varieties:
    print(tea)
```

### Customizing Print Output
```python
# Print on same line with custom separator
for tea in tea_varieties:
    print(tea, end=" - ")
# Output: Black Tea - Green Tea - Oolong Tea -

# Print with numbering
for i, tea in enumerate(tea_varieties):
    print(f"{i+1}. {tea}")
# Output:
# 1. Black Tea
# 2. Green Tea
# 3. Oolong Tea
```

### While Loop with Lists
```python
tea_varieties = ["Black Tea", "Green Tea", "Oolong Tea"]
i = 0

while i < len(tea_varieties):
    print(tea_varieties[i])
    i += 1
```

---

## Conditional Statements

### Checking if Item Exists
```python
tea_varieties = ["Black Tea", "Green Tea", "Oolong Tea"]

# Check if item exists
if "Oolong Tea" in tea_varieties:
    print("I have Oolong tea")
else:
    print("I don't have Oolong tea")

# Check if item doesn't exist
if "Earl Grey" not in tea_varieties:
    print("I don't have Earl Grey")
```

### Conditional Logic with Lists
```python
tea_varieties = ["Black Tea", "Green Tea"]

# Check if list is empty
if tea_varieties:
    print("I have some tea varieties")
else:
    print("No tea varieties available")

# Check list length
if len(tea_varieties) > 2:
    print("I have many tea varieties")
elif len(tea_varieties) > 0:
    print("I have some tea varieties")
else:
    print("No tea varieties")
```

---

## Advanced Concepts

### Range Function
The `range()` function generates sequences of numbers:

```python
# Basic range
print(list(range(5)))        # Output: [0, 1, 2, 3, 4]
print(list(range(1, 6)))     # Output: [1, 2, 3, 4, 5]
print(list(range(0, 10, 2))) # Output: [0, 2, 4, 6, 8]

# Using range in loops
for i in range(5):
    print(f"Number: {i}")
```

### List Comprehension
A concise way to create lists using loops and expressions:

#### Basic Syntax
```python
new_list = [expression for item in iterable]
```

#### Examples
```python
# Create squared numbers
squared_nums = [x**2 for x in range(10)]
# Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Create cubed numbers
cube_numbers = [y**3 for y in range(5)]
# Result: [0, 1, 8, 27, 64]

# Filter and transform
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# Result: [0, 4, 16, 36, 64]

# String operations
uppercase_teas = [tea.upper() for tea in tea_varieties]
```

#### Equivalent Traditional Loop
```python
# List comprehension
squared_nums = [x**2 for x in range(5)]

# Traditional approach
squared_nums = []
for x in range(5):
    squared_nums.append(x**2)
```

### Nested Lists
```python
# 2D list (matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements
print(matrix[0])     # Output: [1, 2, 3]
print(matrix[0][1])  # Output: 2

# List comprehension with nested lists
flattened = [item for sublist in matrix for item in sublist]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## Key Takeaways

### Memory Management
1. **Lists are mutable** - they can be changed after creation
2. **Assignment creates references** - use `.copy()` for actual copies
3. **Understanding references** prevents unexpected behavior

### Indexing and Slicing
1. **Zero-based indexing** - first element is at index 0
2. **Negative indexing** - use -1 for last element, -2 for second-to-last
3. **Slicing is powerful** - can select ranges and modify multiple elements
4. **Slice assignment gotchas** - strings are treated character by character

### Methods and Operations
1. **Multiple methods available** - append, insert, remove, pop, copy
2. **In-place vs returning methods** - some modify the list, others return values
3. **List comprehension** - elegant way to create lists with logic

### Best Practices
1. Use descriptive variable names
2. Prefer `.copy()` when you need independent lists
3. Use list comprehension for simple transformations
4. Be aware of reference vs copy behavior
5. Use appropriate methods for adding/removing elements

---

## Practice Exercises

### Exercise 1: Basic Operations
```python
# Create a list of your favorite movies
movies = ["Movie1", "Movie2", "Movie3"]

# Add a new movie at the end
# Add a movie at the beginning
# Remove a movie from the middle
# Print the final list
```

### Exercise 2: List Comprehension
```python
# Create a list of even numbers from 0 to 20 using list comprehension
# Create a list of squares of odd numbers from 1 to 10
# Create a list of lengths of strings in a given list
```

### Exercise 3: Slicing Practice
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get the first 3 elements
# Get the last 3 elements  
# Get every other element
# Reverse the list using slicing
# Replace elements 3-5 with new values
```

### Exercise 4: Real-world Application
```python
# Create a shopping list program that:
# 1. Allows adding items
# 2. Allows removing items
# 3. Shows the current list
# 4. Counts total items
# 5. Checks if a specific item exists
```

---

## Next Steps

The next topic will cover **Dictionaries** in Python, which store key-value pairs and provide another powerful way to organize and access data.

### Recommended Practice
1. Try all the code examples in this document
2. Complete the practice exercises
3. Experiment with list comprehensions
4. Practice the difference between references and copies
5. Build small programs using lists

---

*Happy Learning! 🐍*