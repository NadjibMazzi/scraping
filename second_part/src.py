import random
import inspect
def random_gen():
    while True:
        num = random.randint(10, 20)
        yield num
        if num == 15:
            break

    pass



def decorator_to_str(func):
    # todo exercise 2
    def inner(*args):
        result = func(args)
        result = str(result)
        return result

    return func


@decorator_to_str
def add(a, b):
    return str(a + b)


@decorator_to_str
def get_info(d):
    return str(d['info'])



def ignore_exception(exception):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception:
                return None

        return wrapper

    return decorator

# Decorate the div function to handle ZeroDivisionError
@ignore_exception(ZeroDivisionError)
def div(a, b):
    return a / b

@ignore_exception(TypeError)
def raise_something(exception):
    raise exception



# exercise 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""

    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap



class MetaInherList(type):
    # todo exercise 5
    pass
    def __new__(cls, name, bases, attrs):
        # Inherit from the built-in list class
        bases = (list,)
        return super().__new__(cls, name, bases, attrs)


class Ex:
    x = 4


class ForceToList(Ex, metaclass=MetaInherList):
    pass
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = 4


class ProcessCheckMeta(type):
    def __init__(cls, name, bases, attrs):
        super(ProcessCheckMeta, cls).__init__(name, bases, attrs)

        # Check if 'process' attribute exists and is a method
        if 'process' in attrs and callable(attrs['process']):
            process_func = attrs['process']
            if len(inspect.signature(process_func).parameters) != 3:
                raise ValueError(f"Class {name} has a 'process' method, but it doesn't take exactly 3 arguments.")

class ExampleClassWithProcessMethod(metaclass=ProcessCheckMeta):
    def process(self, arg1, arg2):
        # This class has a 'process' method with 2 arguments, which should raise a ValueError
        pass

class ExampleClassWithCorrectProcessMethod(metaclass=ProcessCheckMeta):
    def process(self, arg1, arg2, arg3):
        # This class has a 'process' method with 3 arguments, which is correct
        pass
