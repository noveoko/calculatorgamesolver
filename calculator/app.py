import random

class Round:
    def __init__(self, moves=[], goal=0, list_of_buttons=[]):
        self.moves = moves
        self.goal = goal
        self.list_of_buttons = list_of_buttons
    
class Utilities:
    def parseButtons(list_of_buttons):
        symbols = ['+','x','/']
        pass

    def listToNumber(list_of_numbers):
        return int("".join([str(a) for a in list_of_numbers]))

    def generateRecipe(seed=None, moves=2):
        def getItem(key, value):
            nlist = [key]
            if value['takesNum'] == True: #return a number
                nlist.append(random.choice(range(1,9)))
            return tuple(nlist)

        buttons = {'add':{'object':Interface.add, 'weight':1,'takesNum':True},
                   'minus':{'object':Interface.minus, 'weight':1,'takesNum':True},
                   'multiply':{'object':Interface.multiply, 'weight':0.96,'takesNum':True},
                   'divide':{'object':Interface.divide, 'weight':0.95,'takesNum':True},
                   'removeDigit':{'object':Interface.removeDigit, 'weight':0.2,'takesNum':False},
                   'firstDigitToSecond':{'object':Interface.firstDigitToSecond, 'weight':0.1,'takesNum':False},
                   'sumNumbers':{'object':Interface.sumNumbers, 'weight':0.5,'takesNum':False},
                   'invX':{'object':Interface.invX, 'weight':0.01,'takesNum':False}}
        if not seed:
            data = random.choices(population=[getItem(k,v) for k,v in buttons.items()],weights=[v['weight'] for k,v in buttons.items()], k=moves)
        else:
            random.seed(seed)
            data = random.choices(population=[getItem(k,v) for k,v in buttons.items()],weights=[v['weight'] for k,v in buttons.items()], k=moves)
        return data

    def generateGoal():
        
class Interface:

    def __init__(self, number=0):
        self.number = number

    # `+` button
    def add(inputNum, list_of_digits):
        number = Utilities.listToNumber(list_of_digits)
        return number + inputNum

    # `-` button
    def minus(inputNum , list_of_digits):
        number = Utilities.listToNumber(list_of_digits)
        return number - inputNum

    # `x` or `*` button
    def multiply(inputNum, list_of_digits):
        number = Utilities.listToNumber(list_of_digits)
        return number * inputNum

    # `/` button
    def divide(inputNum, list_of_digits):
        number = Utilities.listToNumber(list_of_digits)
        return number / inputNum

    # `<<` button
    def removeDigit(list_of_digits):
        list_of_digits.pop()
        return list_of_digits

    # `1=>2` button
    def firstDigitToSecond(list_of_digits):
        def returnNumber(inputnum ,number_1, number_2):
            if inputnum == number_1:
                return number_2
            else:
                return inputnum
        if len(list_of_digits) >= 2:
            first_digit = list_of_digits[0]
            second_digit = list_of_digits[1]
            return [returnNumber(a, first_digit, second_digit) for a in list_of_digits]
        elif len(list_of_digits) == 1:
            return list_of_digits
        else:
            return 'problem with list input'

    # `SUM` button
    def sumNumbers(list_of_numbers):
        return sum(list_of_numbers)

    def storeNumber(self, number):
        self.number = number

    def invX(list_of_digits,x=10):
        return [a-x for a in list_of_digits]

# – [+]1 adds that number to all the buttons.

