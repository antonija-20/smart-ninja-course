from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import math

url = "https://en.wikipedia.org/wiki/Game_of_Thrones#Adaptation_schedule"

response = urlopen(url).read()
soup = BeautifulSoup(response)

table = soup.findAll("table", attrs={"class": "wikitable"})[0]
links = table.findAll("a")

dataSum = []
sum = 0
seasonLink = 0
row = 0

for link in links:
    wantedString = "(season"
    if wantedString in link.get("href"):
        seasonLink = "https://en.wikipedia.org%s" % link["href"]
        # Concatenate and make a new URL
        print seasonLink
        #print "."
        seasons = BeautifulSoup(urlopen(seasonLink).read()).find("table", attrs={"class": "wikitable plainrowheaders wikiepisodetable"})
        rows = seasons.findAll("sup", attrs={"class": "reference"})

        for row in rows:

            if len(row.parent.contents[0]) != 1:

                row = row.parent.contents[0]
                row = float(row)

            print row


            #row = float(row)
            #print row #dataSum.append(row)


    #print dataSum


#https://stackoverflow.com/questions/482410/how-do-i-convert-a-string-to-a-double-in-python
