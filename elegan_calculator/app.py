import math
from itertools import product

class Calculator:

    def add(numbers=[0],balance=0):
        num = numbers[0]
        return int(num + balance)

    def subtract(numbers=[0],balance=0):
        return int(balance - numbers[0])

    def multiply(numbers=[0],balance=0):
        return int(numbers[0] * balance)

    def divide(numbers=[0],balance=0):
        try:
            return int(balance/numbers[0])
        except ZeroDivisionError as de:
            print("line 20", de)
            return None

    # <<
    def remove_digit(numbers=[0],balance=0):
        if balance != 0:
            bal = [a for a in str(balance)]
            bal.pop()
            return int("".join(bal))
        else:
            return int(balance)

    # `1=>2` button
    def first_digit_to_second(numbers=[0],balance=0):
        numbers = [abs(num) for num in numbers]
        if balance !=0:
            number_string = str(balance)
            left_num = str(numbers[0])
            right_num = str(numbers[1])
            new_values = int(number_string.replace(left_num, right_num))
            return new_values
        else:
            return int(balance)
    
    def storeNumber(numbers=[0],balance=0):
        pass

    def sum_numbers(numbers=[0],balance=0):
        bal = abs(balance)
        return int(sum([abs(int(a)) for a in str(bal)]))

    def inverse_x(balance=0,x=10):
        bal = abs(balance)
        numbers = [x-int(a) for a in str(bal)]
        return int("".join([str(a) for a in numbers]))

    def insert_number(numbers=[0],balance=0):
        if balance != 0:
            bal = [a for a in str(balance)]
            bal.extend(str(numbers[0]))
            return int("".join(bal))
        else:
            return numbers[0]

def solver(goal=None, moves=None,balance=None,buttons=None):
    search_space = [b for b in product(buttons, repeat = moves)]
    for list_of_moves in search_space:
        bal = balance
        for move in list_of_moves:
            button = move[0]
            numbers = move[1]
            bal = getattr(Calculator, button)(numbers=numbers ,balance=bal)
        if bal == goal:
            print('SOLVED!')
            return list_of_moves
            break
    return f'NO MATCH for {buttons}'


if __name__ == "__main__":
    solver(goal=9, moves=5, balance=50, buttons=[('divide',[5]),('multiply',[3]),('remove_digit',[])])

