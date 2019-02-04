import re
from itertools import permutations
from itertools import cycle

class Parse:

    def extract_buttons(self, string_of_buttons):
        """takes a string '+2,+5,/7' and converts it to button tuples"""
        buttons = set()
        s = string_of_buttons
        r = re.compile("((?P<add>\+\d+)|(?P<multiply>x\d+)|(?P<divide>\/\d+)|(?P<balance>\(\d+\))|(?P<subtract>\-\d+)|(?P<delete_last>\<\<)|(?P<replace_num>\d+\=\>\d+)|(?P<insert_number>\d))")
        result = [m.groupdict() for m in r.finditer(s)]
        for dct in result:
            for k,v in dct.items():
                if v:
                    buttons.add((k,v))
        return buttons

class Calculator:
    
      # `+` button
    @staticmethod
    def add(self, inputNum, balance):
        return balance + inputNum

    # `-` button
    @staticmethod
    def minus(self, inputNum , balance):
        return balance - inputNum

    # `x` or `*` button
    @staticmethod
    def multiply(self, inputNum, balance):
        return balance * inputNum

    # `/` button
    @staticmethod
    def divide(self, inputNum, balance):
        return balance / inputNum

    # `<<` button
    @staticmethod
    def removeDigit(self, balance):
        return str(balance)[0:-2] 

    # `1=>2` button
    @staticmethod
    def firstDigitToSecond(self, balance, firstNum, secondNum):
        """Replaces all occurances of first number with second number"""
        return str(balance).replace(str(firstNum),str(secondNum))

    # `SUM` button
    @staticmethod
    def sumNumbers(self, balance):
        return sum([int(a) for a in str(balance)])

    @staticmethod
    def storeNumber(self, number):
        pass

    @staticmethod
    def invX(self, balance,x=10):
        pass

class Solver:
    
    @staticmethod
    def findSolution(data):
        """takes a list of tuples [('add',3),('subtract',9)], balance, moves, and goal
        and outputs a solution or None if no solution is available"""
        buttons = list(data['buttons'])
        c = cycle(buttons)
        if len(buttons) < data['moves']:
            buttons.append(next(c))
        return buttons

    
if __name__ == "__main__":
    pass