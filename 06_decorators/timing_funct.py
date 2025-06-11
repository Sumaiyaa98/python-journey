import time  # We import time to measure how long a function takes to run

# This is our decorator function
def timer(func):
    # This inner function wraps around the original function
    def wrapper(*args, **kwargs):  # Accepts any arguments the original function might need
        start = time.time()  # Record the start time before the function runs
        result = func(*args, **kwargs)  # Call the original function
        end = time.time()  # Record the end time after the function finishes
        print(f"{func.__name__} ran in {end - start} seconds")  # Print how long it took
        return result  # Return the result of the original function
    return wrapper  # Return the wrapper function

# We apply the @timer decorator to the example_function
@timer
def example_function(n):
    time.sleep(n)  # This simulates a task that takes `n` seconds to complete

# Now we call the decorated function
example_function(2)  # This will print how long the function took to run (approx 2 seconds)
