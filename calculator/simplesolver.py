import app
import itertools

def findSolution():
    game = app.Round()
    print(game)
    attempt = game.play()
    print(attempt)
    uniqueMoves = []

    moves = attempt['moves']
    target = attempt['target']
    balance = attempt['balance']
    recipe = attempt['recipe']

    for move in recipe:
        if move not in uniqueMoves:
            print(move)
            uniqueMoves.append(move)
    full_set = []
    while len(full_set) < moves:
        full_set.extend(uniqueMoves)

    template = f'''Balance: {balance}\n
    Player Sees: {uniqueMoves}\n
    Solution: {balance} {recipe} = {target}'''

#    assert len(play_space) == size
    for item in itertools.permutations(full_set, moves):
        result = app.Utilities.generateGoal(item,balance)
        if result == target:
            print(f"SOLUTION: {balance} > {item} = {target}")
            break

if __name__ == "__main__":
    findSolution()
