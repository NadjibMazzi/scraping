import pytest
import unittest

from second_part.src import div, raise_something, add, ForceToList, random_gen, get_info, CacheDecorator, ProcessCheckMeta, ExampleClassWithProcessMethod, ExampleClassWithCorrectProcessMethod


def test_generator():
    g = random_gen()
    assert isinstance(g, type((x for x in [])))
    a = next(g)
    while a != 15:
        assert 10 <= a <= 20
        a = next(g)
    with pytest.raises(StopIteration):
        next(g)


def test_to_str():
    assert add(5, 30) == '35'
    assert get_info({'info': [1, 2, 3]}) == '[1, 2, 3]'


def test_ignore_exception():
    assert div(10, 2) == 5
    assert div(10, 0) is None
    assert raise_something(TypeError) is None
    with pytest.raises(NotImplementedError):
        raise_something(NotImplementedError)

def test_meta_list():
    test = ForceToList([1, 2])
    assert test[1] == 2
    assert test.x == 4



class TestCacheDecorator(unittest.TestCase):
    def test_cache_decorator_caches_result(self):
        cache_decorator = CacheDecorator()

        @cache_decorator
        def add(a, b):
            return a + b

        result1 = add(2, 3)
        result2 = add(2, 3)

        self.assertEqual(result1, result2)

    def test_cache_decorator_caches_result_with_different_parameters(self):
        cache_decorator = CacheDecorator()

        @cache_decorator
        def add(a, b):
            return a + b

        result1 = add(2, 3)
        result2 = add(4, 5)

        self.assertNotEqual(result1, result2)

    def test_cache_decorator_handles_multiple_functions(self):
        cache_decorator = CacheDecorator()

        @cache_decorator
        def add(a, b):
            return a + b

        @cache_decorator
        def multiply(a, b):
            return a * b

        result1 = add(2, 3)
        result2 = multiply(2, 3)

        self.assertEqual(result1, add(2, 3))
        self.assertEqual(result2, multiply(2, 3))

    def test_cache_decorator_handles_multiple_function_calls(self):
        cache_decorator = CacheDecorator()

        @cache_decorator
        def add(a, b):
            return a + b

        result1 = add(2, 3)
        result2 = add(4, 5)

        self.assertEqual(result1, add(2, 3))
        self.assertEqual(result2, add(4, 5))

    def test_cache_decorator_does_not_cache_across_instances(self):
        cache_decorator1 = CacheDecorator()
        cache_decorator2 = CacheDecorator()

        @cache_decorator1
        def add(a, b):
            return a + b

        @cache_decorator2
        def multiply(a, b):
            return a * b

        result1 = add(2, 3)
        result2 = multiply(2, 3)

        self.assertNotEqual(result1, result2)


