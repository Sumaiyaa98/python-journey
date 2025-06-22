def login_required(func):
    def wrapper(*args,**kwargs):
        if 'is_logged_in' in kwargs and kwargs['is_logged_in']:
                return func(*args, **kwargs)
        else:
            return 'You must be logged in to access this.'
    return wrapper
                  
        

@login_required
def view_profile(user_name,is_logged_in):
    return f"Welcome, {user_name}! Here's your profile."
    

print(view_profile('Alex',is_logged_in=False))
print(view_profile('Alex',is_logged_in=True))

