# List of tea varieties
tea_list = ['white', 'black', 'green', 'lemon']

# View all attributes/methods available for a list (used for reference only)
print(tea_list.__dir__)

# --------------------------------------------
# Replace element with a new element in list
tea_list[0] = "Mint"
print(tea_list)  # Output: ['Mint', 'black', 'green', 'lemon']

# Another way using slicing
tea_list[2:3] = ["Ginger"]
print(tea_list)  # Output: ['Mint', 'black', 'Ginger', 'lemon']

# --------------------------------------------
# Insert new element in list at a specific position
tea_list[1:1] = ['Masala']
print(tea_list)  # Output: ['Mint', 'Masala', 'black', 'Ginger', 'lemon']

# Note: Since the start and end index is the same, no element is replaced — it's an insertion

# --------------------------------------------
# Delete elements from list using slicing
tea_list[1:3] = []
print(tea_list)  # Output: ['Mint', 'Ginger', 'lemon']

# --------------------------------------------
# Looping through the list
for tea in tea_list:
    print(tea)

# --------------------------------------------
# Append new element to the end of list
tea_list.append('Tulsi')
print(tea_list)  # Output: ['Mint', 'Ginger', 'lemon', 'Tulsi']

# --------------------------------------------
# Insert element at a specific index
tea_list.insert(1, 'Chamomile')
print(tea_list)  # Output: ['Mint', 'Chamomile', 'Ginger', 'lemon', 'Tulsi']

# --------------------------------------------
# Remove element by value
tea_list.remove('lemon')
print(tea_list)  # Output: ['Mint', 'Chamomile', 'Ginger', 'Tulsi']

# --------------------------------------------
# Pop element (removes and returns last item by default)
last_tea = tea_list.pop()
print(last_tea)   # Output: 'Tulsi'
print(tea_list)   # Output: ['Mint', 'Chamomile', 'Ginger']

# --------------------------------------------
# Count occurrence of an element
tea_list.append('Mint')
print(tea_list.count('Mint'))  # Output: 2

# --------------------------------------------
# Find index of an element
print(tea_list.index('Ginger'))  # Output: 2

# --------------------------------------------
# Reverse the list
tea_list.reverse()
print(tea_list)  # Output: ['Mint', 'Ginger', 'Chamomile', 'Mint']

# --------------------------------------------
# Sort the list alphabetically
tea_list.sort()
print(tea_list)  # Output: ['Chamomile', 'Ginger', 'Mint', 'Mint']

# --------------------------------------------
# Clear all elements from the list
tea_list.clear()
print(tea_list)  # Output: []

# --------------------------------------------
# Copy the list
tea_list = ['white', 'black', 'green']
copy_list = tea_list.copy()
print(copy_list)  # Output: ['white', 'black', 'green']

# --------------------------------------------
# Extend list with another list
extra_tea = ['lemon', 'ginger']
tea_list.extend(extra_tea)
print(tea_list)  # Output: ['white', 'black', 'green', 'lemon', 'ginger']


num_list = [x**2 for x in range(10)]
print(num_list)  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]