from BeautifulSoup import BeautifulSoup

import requests

page = requests.get('https://scrapebook22.appspot.com/')

csv_file = open("kontakti.csv", "w+")

soup = BeautifulSoup(page.content)
print soup.html.head.title.string

seznam_kontaktov = []

for link in soup.findAll("a"):
    if link.string == "See full profile":

        osebna_stran = requests.get("https://scrapebook22.appspot.com/" + link["href"])

        osebna_stran_soup = BeautifulSoup(osebna_stran.content)

        ime_priimek = osebna_stran_soup.find("div", attrs={"class": "col-md-8"}).h1.string
        email = osebna_stran_soup.find("span", attrs={"class": "email"}).string
        kraj_bivanja = osebna_stran_soup.find("span", attrs={"data-city": True}).string

        print ime_priimek + " ; " + email + " ; " + kraj_bivanja

        oseba = ime_priimek + " ; " + email + " ; " + kraj_bivanja

        seznam_kontaktov.append(oseba)

        csv_file.write(ime_priimek + "," + email + "," + kraj_bivanja + "\n")

csv_file.close()

print " "
print "Scraping podatkov narejen...END"

