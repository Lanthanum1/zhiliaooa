from flask import url_for,redirect,g
from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not g.user:
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return wrapper