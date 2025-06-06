# Mutable and Immutable in Python

username = "Alex"
print(username)  # Output: Alex

username = "Mike"
print(username)  # Output: Mike

# Immutable (Example: Strings)
# In Python, immutable means that the value of an object cannot be changed after it is created. Strings are immutable.

# In the example above:

# When we assign "Alex" to username, a new string object "Alex" is created in memory, and the variable username points to it.

# When we assign "Mike" to username, Python does not change the string "Alex". Instead, it creates a new string object "Mike" 
# and changes the reference of the variable username to point to this new string.

# The original string "Alex" still exists in memory (until garbage collected), but username no longer refers to it.

# So, we are not modifying the original value. We are just reassigning the variable to a new object.