from app import Interface


def generateGoal(list_of_moves, start_number=10):
    balance = start_number
    value = 0
    balance, value = None, None
    'add':balance + Interface.add(balance, value),
    'minus':balance + Interface.minus(balance, value),
    'multiply':balance + Interface.multiply(balance, value),
    'divide':balance + Interface.divide(balance, value),
    'removeDigit':Interface.removeDigit(balance),
    'firstDigitToSecond':Interface.firstDigitToSecond(balance),
    'sumNumbers':Interface.sumNumbers(balance),
    'invX':Interface.invX(balance)}
    for item in list_of_moves:
        if len(item) == 2:
            print('2')
        else:
            print('1')

        # if len(item) == 2:
        #     value = item[1]
        #     balance = item[0]
        #     actions[item]
    #return balance

generateGoal([('add','5'),('add',3)],1)