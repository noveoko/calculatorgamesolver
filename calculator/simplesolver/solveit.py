# solveit.py
from process import Calculator
from process import Parse
from itertools import permutations
from itertools import cycle

c = Calculator()
p = Parse()

def collect_data():
    collect = {'moves':{'value':0,'tip':'How many button presses are allowed?'}, 
            'goal' :{'value':0,'tip':'What is the final value of balance?'},
            'balance':{'value':0,'tip':'What is the initial balance?'},
            'buttons':{'value':None,'tip':'Which buttons are available? (not including `CLR`, `Daily Hint`, `Settings` and `Tip`)'}}

    for item, data in collect.items():
        #print(data['tip'])
        if item != 'buttons':
            data['value'] = int(input('{}: '.format(item)))
        elif item == 'buttons':
            data['value'] = set([a for a in p.extract_buttons(input('{}: '.format(item)))])
    
    return collect

def find_solution(data):
    """takes a list of tuples [('add',3),('subtract',9)], balance, moves, and goal
    and outputs a solution or None if no solution is available"""
    perm_buttons = list(data['buttons']['value'])
    required_steps = data['moves']['value']
    c = cycle(data['buttons']['value'])
    if len(perm_buttons) < required_steps:
        perm_buttons.append(next(c))
    search_space = permutations(perm_buttons, required_steps)
    for item in search_space:
        print("MOVES ", item)


if __name__ == "__main__":
    pass