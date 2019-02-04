# solveit.py
from calculate import Calculator

c = Calculator()

def solver():
    collect = {'moves':{'value':0,'tip':'How many button presses are allowed?'}, 
            'goal' :{'value':0,'tip':'What is the final value of balance?'},
            'balance':{'value':0,'tip':'What is the initial balance?'},
            'buttons':{'value':'','tip':'Which buttons are available? (not including `CLR`, `Daily Hint`, `Settings` and `Tip`)'}}

    for item, data in collect.items():
        #print(data['tip'])
        data['value'] = input('{}: '.format(item))

    #find solution (it exists) using collected data
    #parse button string



if __name__ == "__main__":
    solver()