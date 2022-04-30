from src import advmiceng1
import pytest

def test_1():
    a = 1
    b = advmiceng1.example.add_one(a)
    assert b == 2
