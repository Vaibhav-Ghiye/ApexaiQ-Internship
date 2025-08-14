
---

# 📊 NumPy, Pandas & Regex in Python

## **NumPy (`np`)**

NumPy is a powerful Python library used for **numerical computing**, supporting **multi-dimensional arrays** and **mathematical operations** like linear algebra, statistics, and random number generation.

### **Main Uses**

* Efficient handling of large datasets
* Mathematical & statistical operations
* Array manipulations

### **Common Functions**

```python
import numpy as np

# Create arrays
arr1 = np.array([1, 2, 3])  # 1D array
arr2 = np.array([[1, 2], [3, 4]])  # 2D array

# Array shape & size
print(arr2.shape)   # (2, 2)

# Mathematical operations
print(np.mean(arr1))  # Average
print(np.min(arr2))   # Minimum value
print(np.max(arr2))   # Maximum value
print(np.sum(arr2))   # Sum of all elements
print(np.sqrt(arr1))  # Square root

# Random numbers
rand_nums = np.random.rand(3)  # 3 random values between 0 and 1
```

---

## **Pandas (`pd`)**

Pandas is used for **data manipulation and analysis**. It provides **Series** (1D) and **DataFrame** (2D) structures with built-in functions for cleaning, processing, and analyzing data.

### **Main Uses**

* Data cleaning & preprocessing
* Data analysis & statistics
* File handling (CSV, Excel, etc.)

### **Common Functions**

```python
import pandas as pd

# Create Series
series = pd.Series([10, 20, 30])

# Create DataFrame
df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})

# Read & write CSV
df = pd.read_csv("data.csv")
df.to_csv("output.csv", index=False)

# Summary & basic info
print(df.head())       # First 5 rows
print(df.tail())       # Last 5 rows
print(df.describe())   # Summary statistics
print(df.info())       # Data types & null values

# Data selection
print(df["Name"])      # Select column
print(df.iloc[0])      # Select first row
```

---

## **NumPy vs Pandas**

| Feature        | NumPy                  | Pandas                                |
| -------------- | ---------------------- | ------------------------------------- |
| Data Structure | Arrays                 | DataFrames & Series                   |
| Usage          | Numerical computations | Data analysis & manipulation          |
| Speed          | Faster                 | Slightly slower due to extra features |
| Functions      | Math & statistical ops | Filtering, grouping, merging, etc.    |

---

## **Regular Expressions (Regex)**

Regex (**Regular Expressions**) is used to **search, match, and manipulate strings** based on patterns. Python provides the `re` module for regex operations.

### **Common Functions**

```python
import re

text = "My phone number is 9876543210"

# Match at start
print(re.match(r"My", text))

# Search anywhere
print(re.search(r"\d{10}", text))  # Matches 10 digits

# Find all matches
print(re.findall(r"\d", text))  # All digits

# Replace
print(re.sub(r"\d", "*", text))  # Replace digits with '*'

# Split
print(re.split(r"\s", text))  # Split by whitespace
```

---

### **Regex Meta-characters**

## Regex Meta-characters

| Pattern   | Description |
|-----------|-------------|
| `.`       | Matches any character except a newline |
| `^`       | Matches the start of a string |
| `$`       | Matches the end of a string |
| `[]`      | Matches any character inside the brackets |
| `*`       | Matches 0 or more occurrences |
| `+`       | Matches 1 or more occurrences |
| `?`       | Matches 0 or 1 occurrence |
| `{n,m}`   | Matches between n and m occurrences |
| `\d`      | Matches any digit (0-9) |
| `\D`      | Matches any non-digit |
| `\w`      | Matches any alphanumeric character (a-z, A-Z, 0-9, _) |
| `\W`      | Matches any non-alphanumeric character |
| `\s`      | Matches any whitespace (space, tab, newline) |
| `\S`      | Matches any non-whitespace character |

---

