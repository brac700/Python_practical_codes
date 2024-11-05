

import functools

# A sample function that returns user permissions
def get_current_user_permissions():
    # Let's assume the current user has the following permissions
    return ['admin', 'editor']

def requires_permission(permission):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_permissions = get_current_user_permissions()
            if permission in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError("You do not have permission to access this resource.")
        return wrapper
    return decorator

@requires_permission('admin')
def delete_user(user_id):
    print(f"User {user_id} deleted")

# Run the function
delete_user(123)