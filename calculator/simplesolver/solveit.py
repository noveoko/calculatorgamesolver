# solveit.py
from process import Calculator
from process import Parse
from itertools import permutations
from itertools import cycle

c = Calculator()
p = Parse()

def collectData():
    collect = {'moves':{'value':0,'tip':'How many button presses are allowed?'}, 
            'goal' :{'value':0,'tip':'What is the final value of balance?'},
            'balance':{'value':0,'tip':'What is the initial balance?'},
            'buttons':{'value':'','tip':'Which buttons are available? (not including `CLR`, `Daily Hint`, `Settings` and `Tip`)'}}

    for item, data in collect.items():
        #print(data['tip'])
        if item != 'buttons':
            data['value'] = input('{}: '.format(item))
        elif item == 'buttons':
            data['buttons'] = set([a for a in p.extract_buttons(input('{}: '.format(item)))])

    return collect



if __name__ == "__main__":
    pass