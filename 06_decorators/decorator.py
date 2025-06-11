# 🧁 What are decorators?
# Think of decorators like toppings on a cake 🍰.

# You already have a cake (a function), but you want to add something extra — like chocolate chips or icing — without changing the cake recipe itself.

# So a decorator is a function that adds extra features to another function, without changing how that function was originally written.

# 🤔 Why do we use decorators?
# We use decorators when we want to:

# Add extra behavior to a function or method (like logging, checking permissions, etc.)

# Keep our code clean and reusable

# Do something before or after the original function runs

# 💡 A simple example:

def greet():
    return "Hello!"

print(greet())  # Output: Hello!

# Now let’s say we want to make this greeting fancy, but without changing the original greet() function:

def make_fancy(func):
    def wrapper():
        return "🌟 " + func() + " 🌟"
    return wrapper

@make_fancy
def greet():
    return "Hello!"

print(greet())  # Output: 🌟 Hello! 🌟
# Here’s what happened:

# make_fancy is the decorator

# It takes the greet() function and wraps it with some extra stars

# The @make_fancy is just short for doing this: greet = make_fancy(greet)

# 🔍 In short:
# A decorator is a function that takes another function, adds something extra to it, and returns a new one.

# It's like putting a gift wrapper around your original function 🎁

# We use @decorator_name to apply it easily

