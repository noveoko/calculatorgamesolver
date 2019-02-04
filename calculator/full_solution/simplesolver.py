import app
import itertools
import parse

def findSolution(**kwargs):
    if kwargs.get('solution_string'): #parse solution string
        sol_string = kwargs.get('solution_string')
        instructions = parse.parse_solutions(kwargs.get(sol_string))
        print(instructions)
        return instructions

    elif kwargs.get('buttons'): #output a solution
        i = app.Interface()

    """Generates one or more correct solutions to the calculator game"""

    """Takes: balance=0, buttons=List, steps=0, goal=0,solution_string=None"""
    """Balance may be between -1000 and 1000"""
    """Len of available buttons should be between 1 and 10"""
    """Size of steps may be between 1 and 10"""
    """The goal must be between -1000 and 1000"""


    # result = getattr(i, 'add')(4,4)
    # assert result == 8



if __name__ == "__main__":
    findSolution(solution_string='25	2 | 5 | -5 | 5 | +5 = 210')
