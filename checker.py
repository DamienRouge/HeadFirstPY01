from flask import session
from functools import wraps

def check_logged_in(func:'function'):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if 'logged_in' in session:
            return func(*args,**kwargs)#The func is the function below @sign(the decorated function)
        return "You have not yet logged in FROM CHECKER"
    return wrapper
