# ----------------------------
# 🎯 TUPLES IN PYTHON
# ----------------------------

# A tuple is a collection of items which is:
# ✅ Ordered
# ✅ Allows duplicates
# ❌ Immutable (cannot be changed after creation)

# ----------------------------
# 🔸 Creating a Tuple
tea_tuple = ('green', 'black', 'white')
print(tea_tuple)  # Output: ('green', 'black', 'white')

# ----------------------------
# 🔸 Tuple with one item (must add comma)
single_item = ('lemon',)
print(type(single_item))  # Output: <class 'tuple'>

# ----------------------------
# 🔸 Accessing Elements
print(tea_tuple[1])  # Output: black

# ----------------------------
# 🔸 Looping through a tuple
for tea in tea_tuple:
    print(tea)

# ----------------------------
# 🔸 Length of Tuple
print(len(tea_tuple))  # Output: 3

# ----------------------------
# 🔸 Count occurrences of a value
print(tea_tuple.count('black'))  # Output: 1

# ----------------------------
# 🔸 Get index of a value
print(tea_tuple.index('white'))  # Output: 2

# ----------------------------
# 🔸 Tuple with different data types
mixed_tuple = ('Mint', 5, True, 4.5)
print(mixed_tuple)

# ----------------------------
# 🔸 Nested Tuples (Tuple inside a tuple)
nested_tuple = ('herbal', ('ginger', 'tulsi'))
print(nested_tuple[1][0])  # Output: ginger

# ----------------------------
# 🔸 Convert tuple to list (for editing)
tea_list = list(tea_tuple)
tea_list.append('masala')
print(tea_list)  # Output: ['green', 'black', 'white', 'masala']

# ----------------------------
# 🔸 Convert list back to tuple
tea_tuple = tuple(tea_list)
print(tea_tuple)  # Output: ('green', 'black', 'white', 'masala')

# ----------------------------
# 🧠 SHORT DIFFERENCE: LIST vs TUPLE

# LIST
# - Created using square brackets: []
# - Mutable (can be changed)
# - Slower in performance
# - Use when you need to modify data

# TUPLE
# - Created using parentheses: ()
# - Immutable (cannot be changed)
# - Faster in performance
# - Use when data should not change (like days of the week)

# Example:
my_list = ['a', 'b', 'c']
my_tuple = ('x', 'y', 'z')
