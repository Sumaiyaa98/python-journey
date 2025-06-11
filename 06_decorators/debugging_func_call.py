# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.


# This decorator helps in debugging — it prints the function name and arguments each time it's called

def debug(func):
    # Wrapper function that takes any arguments the original function might need
    def wrapper(*args, **kwargs):
        # Converts all positional arguments to string format for printing
        args_val = ", ".join(str(arg) for arg in args)

        # Converts all keyword arguments to "key=value" format for printing
        kwargs_val = ", ".join(f"{k}={v}" for k, v in kwargs.items())

        # Prints the function name and all passed arguments (both positional and keyword)
        print(f"Calling: {func.__name__} with args [{args_val}] and kwargs [{kwargs_val}]")

        # Calls the actual function with the same arguments and returns the result
        return func(*args, **kwargs)
    
    return wrapper  # Returns the wrapper function to replace the original

# We apply the @debug decorator to hello_world
@debug
def hello_world():
    print('Hello World')

# We also apply @debug to greet function, which takes both positional and keyword arguments
@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

# Call the decorated hello_world function — it will show the debug print before the actual print
hello_world()

# Call the decorated greet function — debug output will show the function name, args, and kwargs
greet("Alexander", greeting="Hey")
