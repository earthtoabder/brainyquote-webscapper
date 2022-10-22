import requests
from bs4 import BeautifulSoup as bs
import argparse
from random import choice

page = 1 #change the page if you want
quotes_topic = "Inspirational" # change it to the topic you want
x=8

def Quotes():
    with open("quotes.txt","a+") as file:
        file.write(quotes+"."+"\n")

url = f"https://www.brainyquote.com/search_results?q={quotes_topic}&pg={page}"
r = requests.get(url)
soup = bs(r.content,"html.parser")
anchor1 = soup.find_all('a',{"class":"b-qt"})
anchor2 = soup.find_all('a',{"class":"bq-aut"})
while x > page:
    for i,(quote,author) in enumerate(zip(anchor1,anchor2)):
            quote = quote.find('div').text.strip()
            author = author.text.strip()
            quotes = f"{quote} - {author}"
            Quotes()
            print(quotes)
    page = page+1
        

print("Done!")  