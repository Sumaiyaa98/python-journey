# Problem 3: Cache Return Values
# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

import time

# Decorator that caches function return values
def cache(func):
    cache_value = {}  # A dictionary to store arguments and their corresponding results
    
    # This will just show an empty dictionary at the start
    print(cache_value)

    def wrapper(*args):
        # Check if these arguments were already used before
        if args in cache_value:
            return cache_value[args]  # Return the stored result from cache without running the function again
        
        # If not in cache, call the original function
        result = func(*args)

        # Save the result in cache with args as the key
        cache_value[args] = result

        # Return the newly calculated result
        return result

    return wrapper  # Return the wrapper so it replaces the original function

# Decorate the function with @cache to add caching behavior
@cache
def long_running_function(a, b):
    time.sleep(4)  # Simulate a time-consuming task
    return a + b

# First time calling with (2, 3), it waits 4 seconds and returns 5
print(long_running_function(2, 3))  

# Second time with same arguments, result comes instantly from cache (no delay)
print(long_running_function(2, 3))  

# New arguments (4, 3), so function runs again with 4-second delay
print(long_running_function(4, 3))
