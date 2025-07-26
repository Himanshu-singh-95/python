# Python Tuples - Complete Notes

## What are Tuples?

Tuples are a data structure in Python that store multiple items in a single variable. They are similar to lists but with one crucial difference: **tuples are immutable**.

## Key Differences: Lists vs Tuples

| Feature | Lists | Tuples |
|---------|-------|--------|
| **Syntax** | Square brackets `[]` | Parentheses `()` |
| **Mutability** | Mutable (can be changed) | Immutable (cannot be changed) |
| **Performance** | Slower | Faster (due to immutability) |
| **Use Case** | When data needs to be modified | When data should remain constant |

## Creating Tuples

```python
# Basic tuple creation
tea_types = ("black tea", "green tea", "oolong tea")

# You can also use numbers
numbers = (1, 2, 3, 4, 5)
```

**Remember**: 
- Lists use `[]`
- Dictionaries use `{}`
- Tuples use `()`

## Accessing Tuple Elements

Tuple indexing works exactly like lists:

```python
tea_types = ("black tea", "green tea", "oolong tea")

# Positive indexing (starts from 0)
print(tea_types[0])    # Output: "black tea"
print(tea_types[1])    # Output: "green tea"

# Negative indexing (starts from -1)
print(tea_types[-1])   # Output: "oolong tea"
print(tea_types[-2])   # Output: "green tea"
```

## Slicing Tuples

Slicing works the same way as with lists:

```python
tea_types = ("black tea", "green tea", "oolong tea", "white tea")

print(tea_types[1:3])  # Output: ("green tea", "oolong tea")
print(tea_types[:2])   # Output: ("black tea", "green tea")
print(tea_types[2:])   # Output: ("oolong tea", "white tea")
```

## Immutability - The Key Feature

**Important**: Once a tuple is created, you cannot modify its elements.

```python
tea_types = ("black tea", "green tea", "oolong tea")

# This will cause an ERROR
tea_types[0] = "lemon tea"  # TypeError: 'tuple' object does not support item assignment
```

## Common Tuple Operations

### 1. Getting Length
```python
tea_types = ("black tea", "green tea", "oolong tea")
print(len(tea_types))  # Output: 3
```

### 2. Concatenating Tuples
```python
tea_types = ("black tea", "green tea", "oolong tea")
more_tea = ("herbal tea", "earl grey")

# Combine tuples
all_tea = tea_types + more_tea
print(all_tea)  # Output: ("black tea", "green tea", "oolong tea", "herbal tea", "earl grey")
```

### 3. Membership Testing
```python
all_tea = ("black tea", "green tea", "oolong tea", "herbal tea", "earl grey")

if "green tea" in all_tea:
    print("I have green tea")  # This will print
```

### 4. Counting Elements
```python
more_tea = ("herbal tea", "earl grey", "herbal tea")

count = more_tea.count("herbal tea")
print(count)  # Output: 2

# If element doesn't exist
count = more_tea.count("white tea")
print(count)  # Output: 0
```

## Tuple Unpacking

You can assign tuple elements to individual variables:

```python
tea_types = ("black tea", "green tea", "oolong tea")

# Unpacking
black, green, oolong = tea_types

print(black)   # Output: "black tea"
print(green)   # Output: "green tea"
print(oolong)  # Output: "oolong tea"
```

**Important**: The number of variables must match the number of tuple elements.

## Checking Data Types

```python
tea_types = ("black tea", "green tea", "oolong tea")
print(type(tea_types))  # Output: <class 'tuple'>
```

## Nested Tuples

Just like lists and dictionaries, tuples can be nested:

```python
nested_tuple = (("black tea", "green tea"), ("herbal tea", "white tea"))
print(nested_tuple[0])     # Output: ("black tea", "green tea")
print(nested_tuple[0][1])  # Output: "green tea"
```

## When to Use Tuples

1. **Database Records**: Data from databases often comes as tuples
2. **Coordinates**: Storing x, y coordinates `(10, 20)`
3. **RGB Colors**: Color values `(255, 0, 128)`
4. **Configuration Settings**: Values that shouldn't change during program execution
5. **Performance**: When you need faster access to data that won't change

## Key Takeaways

- Tuples are **immutable** - this is their main feature, not a limitation
- They use **parentheses** `()` for creation
- **Indexing**, **slicing**, and most operations work like lists
- They're **faster** than lists due to immutability
- Perfect for storing data that shouldn't change
- Support **unpacking** for easy variable assignment
- Can be **nested** and **concatenated**

## Practice Tips

1. Use tuples when your data should remain constant
2. Remember: trying to modify a tuple will raise a `TypeError`
3. Tuple unpacking is very useful for functions that return multiple values
4. Practice with different data types (strings, numbers, mixed)

---

*Next Topic*: Continue practicing with tuples and explore more advanced Python data structures!