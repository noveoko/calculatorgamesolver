import random
import itertools

class Round:
    def __init__(self, moves=[], goal=0, list_of_buttons=[]):
        self.moves = moves
        self.goal = goal
        self.list_of_buttons = list_of_buttons

    def play(self, seed=3, moves=13, balance=4):
        recipe = Utilities.generateRecipe(seed, moves)
        target = Utilities.generateGoal(recipe, balance)
        return {'recipe':recipe,'target':target,'balance':balance,'moves':int(moves)}
    
class Utilities:

    @staticmethod
    def parseButtons(list_of_buttons):
        symbols = ['+','x','/','-']
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
    def generateGoal(balance=0,buttons=['x2','+3'],steps=3, end_balance=12):
        parsed_buttons = set()
        for button in buttons:
            
            if 'x' in button:
                parseButtons.add(['multiply',])

        possible = itertools.permutations()


class Interface:

    def __init__(self):
        pass

    def generateMoves(sent_seed=None, moves=4):
        def returnNumber(k,v):
            result = None
            if v['takesNum'] == True:
                random.seed(sent_seed)
                result = (k,random.choice(range(1,10)))
            else:
                result = (k)
            return result

        buttons = {'add':{'weight':1,'takesNum':True},
            'minus':{'weight':1,'takesNum':True},
            'multiply':{'weight':0.96,'takesNum':True},
            'divide':{'weight':0.95,'takesNum':True},
            'removeDigit':{'weight':0.2,'takesNum':False},
            'firstDigitToSecond':{'weight':0.1,'takesNum':False},
            'sumNumbers':{'weight':0.5,'takesNum':False},
            'invX':{'weight':0.01,'takesNum':False}}

        population = [returnNumber(k,v) for k,v in buttons.items()]
        weights = [v['weight']for k,v in buttons.items()]
        random.seed(sent_seed)
        return random.choices(population,weights=weights, k=moves)

    # `+` button
    @staticmethod
    def add(inputNum, balance):
        number = Utilities.listToNumber(balance)
        return number + inputNum

    # `-` button
    @staticmethod
    def minus(inputNum , balance):
        assert inputNum, '`inputNum` must not be empty'
        num = inputNum
        if type(inputNum) is list and inputNum!='':
            num = int("".join(inputNum))
        number = Utilities.listToNumber(balance)
        return number - num

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
            temp = [a for a in str(balance)]
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

if __name__ == "__main__":
    print('app')