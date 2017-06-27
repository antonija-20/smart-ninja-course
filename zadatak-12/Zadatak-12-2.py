from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = "http://quotes.yourdictionary.com/theme/marriage/"

response = urlopen(url).read()
quote_soup = BeautifulSoup(response)

quotes = quote_soup.findAll("p", limit=5, attrs={"class": "quoteContent"})

for quote in quotes:
    print quote.string