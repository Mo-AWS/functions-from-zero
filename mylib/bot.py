import wikipedia

def scrape(name="Wikipedia", length=2):
    result = wikipedia.summary(name, sentences=length)
    return result
