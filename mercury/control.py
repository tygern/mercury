from functools import wraps
from flask import redirect, abort
from mercury.authentication import authentication_service


def requires_auth(api=True):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not authentication_service.logged_in():
                if api:
                    abort(401)
                else:
                    return redirect('/login')

            return f(*args, **kwargs)
        return wrapper
    return decorator
