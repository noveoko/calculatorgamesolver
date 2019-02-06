from itertools import combinations_with_replacement

class Calculator:

    def add(number, balance):
        return number + balance

    def subtract(number, balance):
        return balance - number

    def multiply(number, balance):
        return number * balance

    def divide(number, balance):
        try:
            result = balance/number
            return result
        except ZeroDivisionError as de:
            print(de)
            return None

def solver(goal, moves,balance,buttons):
    search_space = combinations_with_replacement(buttons, moves)
    solution = False
    correct_attempt = None
    for attempt in search_space:
        bal = balance
        for button in attempt:
            bal = getattr(Calculator, button[0])(button[1],bal)
        if bal == goal:
            solution = True
            correct_attempt = attempt
            break
        else:
            print(bal)
            continue
    print(attempt)
    if solution:
        return correct_attempt
    elif not solution:
        return 'cannot find a solution!'



