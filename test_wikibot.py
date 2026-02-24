from wikibot import scrape

def test_scrape(name="Wikipedia", length=2):
    result = scrape(name, length)
    assert isinstance(result, str)
    assert len(result) > 0
