import pytest
import app
from app import Calculator

def test_add():
    assert Calculator.add(3,3) == 6

def test_subtract():
    assert Calculator.subtract(4,10) == 6

def test_multiply():
    assert Calculator.multiply(2, 2) == 4

def test_divide():
    assert Calculator.divide(2, 8) == 4

def test_solver():
    goal = 20
    moves = 4
    balance = 0
    buttons = [('add',2),('add',3),('multiply',2)]
    answer = (('add', 2), ('add', 3), ('multiply', 2), ('multiply', 2))
    assert app.solver(goal,moves,balance,buttons) == answer