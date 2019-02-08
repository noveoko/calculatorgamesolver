import click
import app
import parse

@click.command()
@click.option('--balance',default=0, help='Starting balance')
@click.option('--moves', default=2, help='Number of button events to reach goal')
@click.option('--goal', default=2, help='Target balance')
def collect_data(goal, balance, moves):
    buttons = []
    continue_on = True
    while continue_on:
        print(f'BUTTONS: {buttons}')
        new_button = input('Next Button: ')
        button = parse.parse_all(new_button)
        buttons.append(button)
        decision = input('Would you like to add another button? y or n : ')
        if decision.lower() == 'y':
            continue_on = True
        else:
            continue_on = False
    else:
        print(buttons)
        print(app.solver(goal=goal,moves=moves,balance=balance,buttons=buttons))



if __name__ == '__main__':
    collect_data()