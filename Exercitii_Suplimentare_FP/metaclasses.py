from datetime import datetime


class AdditionMetaClass(type):
    def __init__(cls, name, bases, dict):
        cls.addition = 42
        super().__init__(name, bases, dict)


class MyClass(metaclass=AdditionMetaClass):
    pass


object1 = MyClass.addition
print(object1)

Foo = type('Foo', (), {'attr': 100, 'attr_func': lambda x: x.attr})
x = Foo()
val = x.attr_func()
print(val)


# ------------------------------------------------------------------------------------
# decorators

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Input = (args = {args}, kwargs = {kwargs})")
        print(f"Output = {result}")
        return result

    return wrapper


@decorator
def add(a, b=2):
    return a + b


result = add(3, 5)
print(result)


@decorator
def sub(a=8, b=3):
    return a - b


result = sub(3, 9)
print(result)


def nu_urla_noaptea(func):
    def wrapper():
        if 7 <= datetime.now().hour <= 22:
            func()
        else:
            print("nu urla ca e noapte")

    return wrapper


@nu_urla_noaptea
def urla():
    print("MAAAAAI")


urla()


def total_price(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 10

    return wrapper


@total_price
def price(tax_free_price):
    return tax_free_price


print(price(100))


# def get_information(func):
#     def wrapper():
#         age = int(input('What is your age?'))
#         if age >= 18:
#             func()
#         else:
#             print("You are not eligible to obtain this information")
#     return wrapper
#
# @get_information
# def information():
#     print("Information ...")
#
# information()

def injury(func):
    def wrapper(status):
        if status == 'injured':
            print("Cannot play becuase of injury")
        else:
            func(status)

    return wrapper


@injury
def player_disponibility(status):
    print("Good to go!")


player_disponibility("injured")


def price(func):
    def wrapper(tax_free):
        return 10 + func(tax_free)
    return wrapper


@price
def total_price(tax_free):
    return tax_free


print(total_price(200))
