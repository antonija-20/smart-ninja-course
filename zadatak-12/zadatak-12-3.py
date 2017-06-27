from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = "https://en.wikipedia.org/wiki/Game_of_Thrones#Adaptation_schedule"

response = urlopen(url).read()
soup = BeautifulSoup(response)

table = soup.findAll("table", attrs={"class": "wikitable"})[0]
links = table.findAll("a")

for link in links:
    wantedString = "(season"
    if wantedString in link.get("href"):
        seasonLink = "https://en.wikipedia.org%s" % link["href"]
        # Concatenate and make a new URL
        print seasonLink
        print "."
        seasons = BeautifulSoup(urlopen(seasonLink).read()).find("table", attrs={"class": "wikitable plainrowheaders wikiepisodetable"})
        rows = seasons.findAll("sup", attrs={"class": "reference"})
        for row in rows:
            row = row.parent.contents[0]
            print "Viewers: " + str(row)

        #viewSeason = urlopen(url + link["href"]).read()
        #one = BeautifulSoup(viewSeason)
        #print ".",

        #viewtable = BeautifulSoup(viewSeason).find("table", attrs={"class": "wikitable plainrowheaders wikiepisodetable"})
        #print viewtable

        """
        number = viewtable.findAll("td")
        for item in number:
            print item """




"""for item in response.findAll("a"):
    if item.string == "See full profile":
        #print url + item["href"]

        one = urlopen(url + item["href"]).read()
        soup = BeautifulSoup(one)
        print ".",

        name = soup.findAll("h1")[1].string

        email = soup.findAll("span", attrs={"class": "email"})[0].string

        csv.write(name + "," +email + "\n")

csv.close()
print "\n"
print "CSV je napravljen" """