import click
from mylib.bot import scrape

@click.command()
@click.option('--name', help='The name of the topic to search for.')
@click.option('--length', default=2, help='The number of sentences to return.')
def cli(name='Wikipedia', length=2):
    result = scrape(name, length=length)
    click.echo(click.style(result, bg='white', fg='green', bold=True))

if __name__ == '__main__':
    cli()