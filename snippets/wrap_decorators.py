"""
    Module to show how to wrap external decorator as your own, 
    This will help you to add some custom logic over external decorators or
    to encapsulate the logic with your own implementation
"""

import typing
import functools as ft


def external_decorator(arg_a: int | None = None):
    """this is an external decorator that performs some operation"""

    def decorator(f: typing.Callable):
        @ft.wraps(f)
        def decorated_function(*args, **kwargs):
            print("Inside decorated function")
            rv = (
                operation_a(f(*args, **kwargs))
                if arg_a
                else operation_b(f(*args, **kwargs))
            )
            return rv

        def operation_a(input: typing.Any):
            return str(input) * arg_a  # type: ignore

        def operation_b(input: typing.Any):
            return str(input) * 3

        return decorated_function

    return decorator


@external_decorator()
def my_function(first_number: int, second_number: int):
    """my function to multiply two numbers"""
    return first_number * second_number


print(my_function(5, 8))


def wrap_decorator(arg_a: int):
    """custom wrapper around external decorator which enables external decorator when arg_a is even"""

    def decorator(f: typing.Callable):
        if (arg_a + 1) % 2:
            return external_decorator(arg_a)(f)
        return f

    return decorator


@wrap_decorator(arg_a=3)
def my_second_function(first_number: int, second_number: int):
    """my function to multiply two numbers"""
    return first_number * second_number


print(my_second_function(5, 8))

# Below is sample example for flask-caching which is wrapped inside custom decorator:

# def cached(
#     timeout: int,
#     key_prefix: str = "ada",
#     unless: typing.Callable | None = None,
#     forced_update: typing.Callable | None = None,
#     response_filter: typing.Callable | None = None,
#     query_string: bool = False,
#     hash_method: typing.Callable = hashlib.md5,
#     cache_none: bool = False,
#     make_cache_key: typing.Callable | None = None,
#     source_check: bool | None = None,
#     response_hit_indication: bool | None = False,
# ):
#     def decorator(f: typing.Callable):
#         function = flask_caching.cached(
#             timeout=timeout,
#             key_prefix=key_prefix,
#             unless=unless,
#             forced_update=forced_update,
#             response_filter=response_filter,
#             query_string=query_string,
#             hash_method=hash_method,
#             cache_none=cache_none,
#             make_cache_key=make_cache_key,
#             source_check=source_check,
#             response_hit_indication=response_hit_indication,
#         )
#         return function(f)

#     return decorator
