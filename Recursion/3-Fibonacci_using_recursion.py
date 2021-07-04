""" Fibonacci Sequence using recursion """
def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position -1) + get_fib(position -2)


print(get_fib(4))
"""
Explanation:
get_fib(2) = get_fib(1) + get_fib(0)
           = 1          + 0
           = 1
get_fib(3) = get_fib(2) + get_fib(1)
           = 1          + 1
           = 2
get_fib(4) = get_fib(3) + get_fib(2)
           = 2          + 1
           = 3
"""
