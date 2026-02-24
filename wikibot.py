import wikipedia, click

@click.command()
@click.option('--name', prompt='Wikipedia page to scrape', help='The name of the topic to search for.')
def scrape(name="Wikipedia", length=2):
    result = wikipedia.summary(name, sentences=length)
    click.echo(click.style(result, bg='white', fg='green', bold=True))

if __name__ == '__main__':
    scrape()