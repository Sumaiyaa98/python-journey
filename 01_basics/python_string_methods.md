
# 🔤 Python String Methods with Examples

Below are commonly used string methods in Python, with easy examples.

---

## 📌 1. `upper()`

Converts all characters to uppercase.

```python
text = "hello"
print(text.upper())  # Output: "HELLO"
```

---

## 📌 2. `lower()`

Converts all characters to lowercase.

```python
text = "HELLO"
print(text.lower())  # Output: "hello"
```

---

## 📌 3. `capitalize()`

Capitalizes the first letter of the string.

```python
text = "python is fun"
print(text.capitalize())  # Output: "Python is fun"
```

---

## 📌 4. `title()`

Capitalizes the first letter of each word.

```python
text = "python is fun"
print(text.title())  # Output: "Python Is Fun"
```

---

## 📌 5. `strip()`

Removes leading and trailing whitespaces.

```python
text = "   hello   "
print(text.strip())  # Output: "hello"
```

---

## 📌 6. `replace()`

Replaces a substring with another substring.

```python
text = "I like cats"
print(text.replace("cats", "dogs"))  # Output: "I like dogs"
```

---

## 📌 7. `split()`

Splits a string into a list using a delimiter (default is space).

```python
text = "Python is fun"
print(text.split())  # Output: ['Python', 'is', 'fun']
```

---

## 📌 8. `join()`

Joins elements of a list into a string using a separator.

```python
words = ["Python", "is", "fun"]
print(" ".join(words))  # Output: "Python is fun"
```

---

## 📌 9. `startswith()` and `endswith()`

Checks if a string starts or ends with a specific substring.

```python
text = "hello world"
print(text.startswith("hello"))  # Output: True
print(text.endswith("world"))    # Output: True
```

---

## 📌 10. `find()` and `index()`

Returns the index of the first occurrence of a substring.

- `find()` returns `-1` if not found.
- `index()` raises an error if not found.

```python
text = "hello"
print(text.find("l"))   # Output: 2
print(text.index("l"))  # Output: 2
```

---

## 📌 11. `count()`

Returns how many times a substring appears in the string.

```python
text = "banana"
print(text.count("a"))  # Output: 3
```

---

## 📌 12. `isalpha()`, `isdigit()`, `isalnum()`

Checks character types in the string.

```python
print("abc".isalpha())    # Output: True
print("123".isdigit())    # Output: True
print("abc123".isalnum()) # Output: True
```

---

📎 **Note**: These methods do not change the original string because strings in Python are immutable. They return new strings.
