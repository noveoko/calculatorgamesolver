import pytest
from app import Interface
from app import Round
from app import Utilities
import parse
import math

def test_remove_digits():
    lists = [[0,3,4,5],[0,0],[-23,0,1]]
    assert Interface.removeDigit(lists[0]) == [0,3,4]
    assert Interface.removeDigit(lists[1]) == [0]
    assert Interface.removeDigit(lists[2]) == [-23,0]

def test_first_digit_to_second():
    testList = [[1,2,1,1],[0],[9,9,0]]
    assert Interface.firstDigitToSecond(testList[0]) == [2,2,2,2]
    assert Interface.firstDigitToSecond(testList[1]) == [0]
    assert Interface.firstDigitToSecond(testList[2]) == [9,9,0]

def test_sum_of_numbers():
    testList = [2,3,1]
    assert Interface.sumNumbers(testList) == 6

def test_store_number():
    test_number = 5
    a = Interface()
    result = a.storeNumber(test_number)
    assert result == None

def test_invx():
    testLists = [[0],[-1,5,0,0]]
    assert Interface.invX(testLists[0], 10) == [-10]
    assert Interface.invX(testLists[1], 10) == [-11, -5, -10, -10]

def test_add():
    test_list = [3,4,4]
    assert Interface.add(6, test_list) == 350

def test_minus():
    test_list = [3,4,4]
    assert Interface.minus(4, test_list) == 340

def test_multiply():
    test_list = [1,0]
    assert Interface.multiply(5, test_list) == 50

def test_divide():
    test_list = [1,0]
    assert Interface.divide(2, test_list) == 5

def test_listToNumber():
    test_data = [[1,2,4,7],4675]
    assert Utilities.listToNumber(test_data[0]) == 1247
    assert Utilities.listToNumber(test_data[1]) == 4675

@pytest.mark.skip(reason="need to fix this by full refactor")
def test_generateGoal():
    tests = [{'moves':[('add', 10),('divide', 2)],
              'output': 410, 
              'balance':200},
             {'moves':[('add', 10),('divide', 2),('multiply', 12)],
              'output': 390, 
              'balance':10},
             {'moves':[('subtract', 10),('invX'),('divide', 12),('firstDigitToSecond'),('add',200)],
              'output': 214, 
              'balance':4}]

    for test in tests:
        moves = test['moves']
        result = Utilities.generateGoal(moves, test['balance'])
        assert math.floor(result) == test['output']

def test_generateRecipeGenerateGoal():
    seed, moves, balance = 3, 5, 30
    moves = Interface.generateMoves(seed, moves)
    goal = Utilities.generateGoal(moves,balance)
    assert goal == 30

def test_parse_solutions():
    '''takes as input solutions available online and outputs dictionary'''
    test = '19	1 | 0 | 1 = 101'
    result = parse.parse_solutions([test])
    assert result == [{'balance': 0, 'steps': ['19\t1 ', ' 0 ', ' 1 '], 'target': ' 101'}]