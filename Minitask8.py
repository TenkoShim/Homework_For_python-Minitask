# Мини-задача #8

# Реализовать декоратор @deprecated, который отмечает
# функцию, как устаревшую.
#
# У декоратора есть два опциональных параметра since и
# will_be_removed.
import functools
def deprecated(func=None, *, since=None, when_removed=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            name = wrapper.__name__

            if since and when_removed:
                message = f"Warning: function {name} is deprecated since version {since}. It will be removed in version {when_removed}"
            elif since:
                message = f"Warning: function {name} is deprecated since version {since}. It will be removed in future"
            elif when_removed:
                message = f"Warning: function {name} is deprecated. It will be removed in version {when_removed}"
            else:
                message = f"Warning: function {name} is deprecated. It will be removed in future versions"

            print(message)
            return func(*args, **kwargs)

        return wrapper

    if func is None:
        return decorator
    else:
        return decorator(func)


@deprecated
def my_function():
    print("This is a deprecated function")


@deprecated(since="1.0")
def another_function():
    print("This is another deprecated function")


@deprecated(when_removed="2.0")
def yet_another_function():
    print("This is yet another deprecated function")


my_function()
another_function()
yet_another_function()
