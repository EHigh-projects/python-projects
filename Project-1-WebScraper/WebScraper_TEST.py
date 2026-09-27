from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com"
headers = { 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9"
    }

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,"html.parser")
quotes = soup.find_all("span", attrs={"text"})
authors = soup.find_all("small", attrs={"author"})

for quote in quotes:
    print(quote.text)
for author in authors:
    print(author.text)