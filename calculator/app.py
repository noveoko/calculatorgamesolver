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
        result = None
        if type(list_of_numbers) == list:
            result = int("".join([str(a) for a in list_of_numbers]))
        elif type(list_of_numbers) == int:
            result = list_of_numbers
        else:
            result = 'Error with listToNumber'
        return result

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
    def generateGoal(list_of_moves, start_number=10):
        interface = Interface()
        balance = start_number
        for item in list_of_moves:
            move = item[0]
            number = None
            if item[1] and type(item[1]) == int:
                if move == 'add':
                    balance += interface.add(balance, item[1])
                elif move == 'minus':
                    balance += interface.minus(balance, item[1])
                elif move == 'multiply':
                    balance += interface.multiply(balance, item[1])
                elif move == 'divide':
                    balance += interface.divide(balance, item[1])
            elif not item[1]:
                if move == 'removeDigit':
                    balance = interface.removeDigit(balance)
                elif move == 'firstDigitToSecond':
                    balance = interface.firstDigitToSecond(balance)
                elif move == 'sumNumbers':
                    balance = interface.sumNumbers(balance)
                elif move == 'invX':
                    balance = interface.invX(balance)
        return balance

class Interface:

    def __init__(self):
        pass

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
    def add(inputNum, balance):
        number = Utilities.listToNumber(balance)
        return number + inputNum

    # `-` button
    @staticmethod
    def minus(inputNum , balance):
        number = Utilities.listToNumber(balance)
        return number - inputNum

    # `x` or `*` button
    @staticmethod
    def multiply(inputNum, balance):
        number = Utilities.listToNumber(balance)
        return number * inputNum

    # `/` button
    @staticmethod
    def divide(inputNum, balance):
        number = Utilities.listToNumber(balance)
        return number / inputNum

    # `<<` button
    @staticmethod
    def removeDigit(balance):
        if type(balance) == list:
            balance.pop()
            return balance
        elif type(balance) == int:
            temp = [str(a) for a in balance.split()]
            temp.pop()
            return temp      

    # `1=>2` button
    @staticmethod
    def firstDigitToSecond(balance):
        def returnNumber(inputnum ,number_1, number_2):
            if inputnum == number_1:
                return number_2
            else:
                return inputnum
        if len(balance) >= 2:
            first_digit = balance[0]
            second_digit = balance[1]
            return [returnNumber(a, first_digit, second_digit) for a in balance]
        elif len(balance) == 1:
            return balance
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
    def invX(balance,x=10):
        return [a-x for a in balance]

# – [+]1 adds that number to all the buttons.

