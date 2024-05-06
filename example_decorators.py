from itertools import count


def polite(name):
    print(f"Good day to you, {name}!")

def familiar(name):
    print(f"Yo, {name}, what's up?")

def greet_bastien(greet_function):
    greet_function("Bastien")

# greet_bastien(polite)

def big_function(num):

    print("....doing lots of stuff...")

    def inner_1():
        print("inside inner_1")
    
    def inner_2():
        print("inside inner_2")
    
    if num == 1:
        return inner_1
    else:
        return inner_2

# result = big_function(2)
# result()
# print(result)

# ------- Decorators --------
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called!")
        func(*args, **kwargs)
        print("After the function is called!")
    
    return wrapper

@decorator
def say_hello(name="Bastien", twice=False):
    print(f"Hello, {name}!")
    if twice:
        print(f"Hello, {name}!")


# say_hello = decorator(say_hello)
say_hello(twice=True)


def test(*args):
    print(args)

data = [4, 5, 6]

test(1, 2, 3, 4, 5, 6, 7, "Top", "Weird", "ok")


def do_multiples(number):
    def inner(func):
        def wrapper(*args, **kwargs):
            for i in range(number):
                func(*args, **kwargs)
        return wrapper
    return inner

@do_multiples(5)
def countdown(n):
    for i in range(n, -1, -1):
        print(i)

countdown(3)

# ---- Debug example ----

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func} with {args}, {kwargs}")
        res = func(*args, **kwargs)
        print(f"Return value: {res}")
        return res
    
    return wrapper

@debug
def testing(word):
    print(word)
    return 6


testing("allo")
import math
math.factorial = debug(math.factorial)
print(math.factorial(5))

