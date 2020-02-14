# Create your tests here.
from django.test import TestCase


def f(x):
    return x+1


def test_function():
    assert f(3) == 4
