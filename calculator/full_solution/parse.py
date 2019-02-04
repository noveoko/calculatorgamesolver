import re


        # buttons = {'add':{'weight':1,'takesNum':True},
        #     'minus':{'weight':1,'takesNum':True},
        #     'multiply':{'weight':0.96,'takesNum':True},
        #     'divide':{'weight':0.95,'takesNum':True},
        #     'removeDigit':{'weight':0.2,'takesNum':False},
        #     'firstDigitToSecond':{'weight':0.1,'takesNum':False},
        #     'sumNumbers':{'weight':0.5,'takesNum':False},
        #     'invX':{'weight':0.01,'


def parse_all(**kwargs):
    if kwargs.get("problem_string"):
        #parse string -> continue processing
        regex = re.compile(r"((?P<add>\+\d+)|(?P<multiply>x\d+)|(?P<divide>\/\d+)|(?P<balance>\(\d+\))|(?P<subtract>\-\d+)|(?P<delete_last>\<\<)|(?P<replace_num>\d+\=\>\d+)|(?P<insert_number>\d))")
        #to_parse = "+6 | 6=>9 | x7 |6=>9"
        results = re.findall(regex, kwargs.get("problem_string"))
        print(results)

def convert_steps(list_of_steps):
    fixed_steps = []
    for step in steps:
        print(step)

def parse_solutions(list_of_solutions=None):
    """takes a list of solutions and outputs a tuple of instructions"""
    results = []
    for sol in list_of_solutions:
        balance = 0
        sections = sol.split("|")
        last_step, target = sections[-1].split("=")
        sections.pop()
        sections.append(last_step)
        if sections[0].startswith("("):#update balance
            balance = int(re.sub(r"[^\d+]","",re.search(r"\(\d+\)", sections[0]).group(0)))
            sections[0] = re.sub(r"\(\d+\)", "", sections[0])
        results.append({'balance':balance, 'steps':[a.lower() for a in sections], 'target':target})
    return results    

def parse_all_solutions(path):
    
    lines = [a.strip() for a in open(path).readlines()]
    for line in lines:
        print(parse_solution(line))

def parse_solution(raw_solution):
    balance = 0
    rest, total = raw_solution.split("=")
    if re.match("\(\d+\)", rest): #contains balance
        balance = re.sub("[^\(\d+\)]", "", rest).group(0)
    steps = 7



if __name__ == "__main__":
    parse_all(problem_string="+6 | 6=>9 | x7 |6=>9".strip())

