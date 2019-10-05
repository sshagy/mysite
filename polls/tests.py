# from django.test import TestCase

# Create your tests here.


def foo():
    return 1
    return 2

print(1111, foo())

def bar():
    yield 1
    yield 2

print(2222, bar())
print(3333, list(bar()))