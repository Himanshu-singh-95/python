# Python Dictionaries - Complete Study Notes

## What are Dictionaries?

Dictionaries are a fundamental data structure in Python that store data in **key-value pairs**. Unlike lists where order matters and elements are accessed by index (0, 1, 2...), dictionaries allow you to access values using meaningful keys.

### Key Differences: Lists vs Dictionaries

| Lists | Dictionaries |
|-------|-------------|
| Order matters | Order doesn't matter |
| Access by index (0, 1, 2...) | Access by custom keys |
| Sequential storage | Key-value mapping |
| `[item1, item2, item3]` | `{"key1": "value1", "key2": "value2"}` |

## Creating Dictionaries

### Method 1: Using Curly Braces `{}`
```python
# Basic dictionary creation
chai_types = {
    "masala": "spicy",
    "ginger": "zesty", 
    "green": "mild"
}
```

### Method 2: Using `dict()` Constructor
```python
chai_types = dict()  # Creates empty dictionary
```

## Accessing Dictionary Values

### Method 1: Square Bracket Notation
```python
chai_types = {"masala": "spicy", "ginger": "zesty"}

# Access value by key
print(chai_types["masala"])  # Output: spicy

# ⚠️ Warning: Raises KeyError if key doesn't exist
print(chai_types["nonexistent"])  # KeyError!
```

### Method 2: `.get()` Method (Safer)
```python
# Safe access - returns None if key doesn't exist
print(chai_types.get("masala"))    # Output: spicy
print(chai_types.get("nonexistent"))  # Output: None
```

## Modifying Dictionaries

### Adding/Updating Values
```python
chai_types = {"masala": "spicy", "ginger": "zesty"}

# Update existing value
chai_types["green"] = "fresh"

# Add new key-value pair
chai_types["earl_grey"] = "citrusy"

print(chai_types)
# Output: {'masala': 'spicy', 'ginger': 'zesty', 'green': 'fresh', 'earl_grey': 'citrusy'}
```

### Removing Items

#### Using `pop()` - Removes specific key
```python
removed_value = chai_types.pop("ginger")  # Returns "zesty"
print(removed_value)  # Output: zesty
```

#### Using `popitem()` - Removes last added item
```python
last_item = chai_types.popitem()  # Returns ('earl_grey', 'citrusy')
print(last_item)
```

#### Using `del` keyword
```python
del chai_types["green"]  # Deletes the key-value pair
```

## Iterating Through Dictionaries

### Method 1: Iterate Over Keys (Default)
```python
chai_types = {"masala": "spicy", "ginger": "zesty", "green": "fresh"}

for chai in chai_types:
    print(chai)  # Prints: masala, ginger, green
```

### Method 2: Iterate Over Keys and Values
```python
for chai in chai_types:
    print(f"{chai}: {chai_types[chai]}")
# Output:
# masala: spicy
# ginger: zesty  
# green: fresh
```

### Method 3: Using `.items()` Method
```python
for key, value in chai_types.items():
    print(f"{key}: {value}")
# Output:
# masala: spicy
# ginger: zesty
# green: fresh
```

## Useful Dictionary Operations

### Check if Key Exists
```python
if "masala" in chai_types:
    print("I have masala chai")
```

### Get Dictionary Length
```python
print(len(chai_types))  # Output: 3
```

### Copy Dictionaries
```python
# Creates a new copy (not a reference)
chai_copy = chai_types.copy()
```

### Clear All Items
```python
chai_types.clear()  # Empties the dictionary
print(chai_types)  # Output: {}
```

## Nested Dictionaries

Dictionaries can contain other dictionaries as values, creating a hierarchical structure.

```python
tea_shop = {
    "chai": {
        "masala": "spicy",
        "ginger": "zesty"
    },
    "tea": {
        "green": "mild",
        "black": "strong"
    }
}

# Accessing nested values
print(tea_shop["chai"]["ginger"])  # Output: zesty
```

## Dictionary Comprehensions

Create dictionaries using a concise syntax (similar to list comprehensions):

```python
# Create a dictionary of squares
squared_nums = {x: x**2 for x in range(6)}
print(squared_nums)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Creating Dictionaries from Lists

### Using `dict.fromkeys()`
```python
keys = ["masala", "ginger", "lemon"]
default_value = "delicious"

# All keys get the same default value
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
# Output: {'masala': 'delicious', 'ginger': 'delicious', 'lemon': 'delicious'}
```

⚠️ **Important Note**: If you pass a list as the default value, all keys will reference the same list object!

## Key Takeaways

1. **Dictionaries are unordered** - Focus on keys, not positions
2. **Keys must be unique** - Duplicate keys will overwrite previous values  
3. **Keys must be immutable** - Use strings, numbers, or tuples as keys (not lists)
4. **Values can be any data type** - Including other dictionaries, lists, etc.
5. **Use `.get()` for safe access** - Prevents KeyError exceptions
6. **Dictionaries are mutable** - Can be modified after creation

## Common Use Cases

- **User information**: `{"name": "John", "age": 25, "city": "Mumbai"}`
- **Configuration settings**: `{"debug": True, "port": 8080}`
- **Database records**: Perfect for NoSQL databases
- **API responses**: JSON data maps directly to Python dictionaries
- **Counting occurrences**: `{"apple": 5, "banana": 3}`

## Practice Exercises

1. Create a dictionary of your favorite movies with genres
2. Build a nested dictionary representing a school with classes and students
3. Use dictionary comprehension to create a multiplication table
4. Practice converting between lists and dictionaries

---

*Remember: Dictionaries are everywhere in Python! They're essential for web development (Django), data analysis, and API interactions. Master them well!*