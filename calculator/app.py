import random

class Round:
    def __init__(self, moves=[], goal=0, list_of_buttons=[]):
        self.moves = moves
        self.goal = goal
        self.list_of_buttons = list_of_buttons
    
class Utilities:

    @staticmethod
    def parseButtons(list_of_buttons):
        symbols = ['+','x','/']
        pass
    @staticmethod
    def listToNumber(list_of_numbers):
        return int("".join([str(a) for a in list_of_numbers]))
    @staticmethod
    def generateRecipe(seed=None, moves=2):
        def getItem(key, value):
            nlist = [key]
            if value['takesNum'] == True: #return a number
                nlist.append(random.choice(range(1,9)))
            return tuple(nlist)
        buttons = Interface.buttons
        if not seed:
            data = random.choices(population=[getItem(k,v) for k,v in buttons.items()],weights=[v['weight'] for k,v in buttons.items()], k=moves)
        else:
            random.seed(seed)
            data = random.choices(population=[getItem(k,v) for k,v in buttons.items()],weights=[v['weight'] for k,v in buttons.items()], k=moves)
        return data

    #takes as input list of lists [button, button_object, number] 
    #returns goal as a list [goalNumber, optimalPath] optimalPath when reversed is the correct solution to a given round
    @staticmethod
    def generateGoal( ):
        pass

class Interface:

    buttons = {'add':{'weight':1,'takesNum':True},
                'minus':{'weight':1,'takesNum':True},
                'multiply':{'weight':0.96,'takesNum':True},
                'divide':{'weight':0.95,'takesNum':True},
                'removeDigit':{'weight':0.2,'takesNum':False},
                'firstDigitToSecond':{'weight':0.1,'takesNum':False},
                'sumNumbers':{'weight':0.5,'takesNum':False},
                'invX':{'weight':0.01,'takesNum':False}}


    # `+` button
    @staticmethod
    def add(inputNum, list_of_digits):
        number = Utilities.listToNumber(list_of_digits)
        return number + inputNum

    # `-` button
    @staticmethod
    def minus(inputNum , list_of_digits):
        number = Utilities.listToNumber(list_of_digits)
        return number - inputNum

    # `x` or `*` button
    @staticmethod
    def multiply(inputNum, list_of_digits):
        number = Utilities.listToNumber(list_of_digits)
        return number * inputNum

    # `/` button
    @staticmethod
    def divide(inputNum, list_of_digits):
        number = Utilities.listToNumber(list_of_digits)
        return number / inputNum

    # `<<` button
    @staticmethod
    def removeDigit(list_of_digits):
        list_of_digits.pop()
        return list_of_digits

    # `1=>2` button
    @staticmethod
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
    @staticmethod
    def sumNumbers(list_of_numbers):
        return sum(list_of_numbers)

    @staticmethod
    def storeNumber(number):
        number = number

    @staticmethod
    def invX(list_of_digits,x=10):
        return [a-x for a in list_of_digits]

# – [+]1 adds that number to all the buttons.

