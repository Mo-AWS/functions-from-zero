from wikibot import scrape
from click.testing import CliRunner

def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(scrape, ['--name', 'Facebook'])
    assert result.exit_code == 0
    assert 'facebook' in result.output
