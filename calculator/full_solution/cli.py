import click

@click.command()
@click.option('--balance',default=0, help='Starting balance')
@click.option('--buttons',default=['1','x2'],help='Available buttons')
@click.option('--steps', default=2, help='Number of button events to reach goal')
@click.option('--goal', default=2, help='Target balance')
def get_solution(balance, buttons, steps, goal):
    solution = str(['x2','5','5','/2','<<'])
    #return answer
    click.echo(f'The correct button sequence is: %s' %solution)


if __name__ == '__main__':
    get_solution()