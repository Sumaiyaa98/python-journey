# enumerate in Python is a built-in function that adds a counter (index number) to each item in an iterable (like a list or tuple) when you loop over it.

# 📌 Why Use enumerate?
# Normally, when looping through a list, you just get the values. But sometimes you also want to know the index (position) of each value.

# ✅ Without enumerate:

fruits = ['apple', 'banana', 'cherry']
index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1

# ✅ With enumerate (shorter and cleaner):

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 🟢 Output:


# 0 apple
# 1 banana
# 2 cherry

x = ['a','b','c']
y = enumerate(x)
print(dict(y))