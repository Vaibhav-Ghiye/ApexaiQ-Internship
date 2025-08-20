# Session by Aditya Sir   

---

## 1. List Comprehension

**What it is:**
A concise way to create lists in Python by combining loops and conditions in a single line.

**Why use it:**

* More readable and compact than traditional loops
* Often faster for simple operations

**Syntax:**

```python
[expression for item in iterable if condition]
```

**Example:**

```python
# Generate squares of even numbers from 1 to 10
squares_even = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares_even)  
# Output: [4, 16, 36, 64, 100]
```

---

## 2. Dict Comprehension

**What it is:**
A shorthand for creating dictionaries by looping through data in one line.

**Why use it:**

* Easy way to transform or filter dictionary data
* Improves readability

**Syntax:**

```python
{key_expression: value_expression for item in iterable if condition}
```

**Example:**

```python
# Create a dictionary with numbers and their cubes
cubes = {x: x**3 for x in range(1, 6)}
print(cubes)  
# Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
```

---

## 3. File Handling

**What it is:**
Working with files (reading, writing, appending) using Python’s built-in functions.

**Why use it:**

* Store data permanently
* Read configuration files, logs, datasets, etc.

**Example:**

```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a file
with open("example.txt", "a") as file:
    file.write("Appending a new line.\n")
```

---

## 4. Error Handling

**What it is:**
Mechanism to handle runtime errors using `try`, `except`, `else`, and `finally`.

**Why use it:**

* Prevents program crashes
* Allows graceful handling of unexpected situations

**Example:**

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")
```

---

### 📄 Final Python Script (All Examples in One File)

```python
# ===== 1. List Comprehension =====
squares_even = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Squares of even numbers:", squares_even)

# ===== 2. Dict Comprehension =====
cubes = {x: x**3 for x in range(1, 6)}
print("Cubes dictionary:", cubes)

# ===== 3. File Handling =====
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")

with open("example.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

with open("example.txt", "a") as file:
    file.write("Appending a new line.\n")

# ===== 4. Error Handling =====
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")
```

---
