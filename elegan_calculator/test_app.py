import pytest
import app
from app import Calculator

def test_add():
    assert Calculator.add(numbers=[3],balance=3) == 6
    assert Calculator.add(numbers=[0],balance=0) == 0

def test_subtract():
    assert Calculator.subtract(numbers=[4],balance=10) == 6

def test_multiply():
    assert Calculator.multiply(numbers=[2], balance=2) == 4

def test_divide():
    assert Calculator.divide(numbers=[8], balance=2) == 0
    assert Calculator.divide(numbers=[0.1], balance=10) == 100

def test_remove_digit():
    assert Calculator.remove_digit(balance=333) == 33
    assert Calculator.remove_digit(balance=0) == 0

def test_first_digit_to_second():
    assert Calculator.first_digit_to_second(numbers=[3,2],balance=23234) == 22224
    assert Calculator.first_digit_to_second(numbers=[2,0],balance=22320) == 300
    assert Calculator.first_digit_to_second(numbers=[1,0],balance=1) == 0
    assert Calculator.first_digit_to_second(numbers=[1,-5],balance=111) == 555
    assert Calculator.first_digit_to_second(numbers=[8,1],balance=1458182133) == 1451112133

def test_sum_numbers():
    assert Calculator.sum_numbers(balance=305) == 8
    assert Calculator.sum_numbers(balance=0) == 0
    assert Calculator.sum_numbers(balance=-60) == 6

def test_inverse_x():
    assert Calculator.inverse_x(balance=111) == 999
    assert Calculator.inverse_x(balance=0) == 10

def test_insert():
    assert Calculator.insert_number(numbers=[2],balance=100) == 1002
    assert Calculator.insert_number(numbers=[333],balance=0) == 333

def test_solver():
    goal = 20
    moves = 4
    balance = 0
    buttons = [('add',[2]),('add',[3]),('multiply',[2])]
    answer = (('multiply', [2]), ('add', [3]), ('add', [3]), ('add', [2]))
    assert app.solver(goal,moves,balance,buttons) == answer

def test_solver_2():
    goal = 29
    moves = 5
    balance = 11
    buttons = [('divide',[2]),('add',[3]),('first_digit_to_second',[1,2]),('first_digit_to_second',[2,9])]
    answer = (('add', [3]),('first_digit_to_second',[1,2]),('divide',[2]),('first_digit_to_second',[2,9]),('first_digit_to_second',[1,2]))
    assert app.solver(goal,moves,balance,buttons) == answer


