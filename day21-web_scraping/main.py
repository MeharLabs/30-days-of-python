# ============================================
# 🐍 Day 21 - Web Scraping
# 📅 Date: 08/05/2026
# 🎯 Goal: Learn how to automatically extract data from websites using Python's requests and BeautifulSoup libraries - HTML parsing, element selection.
# =============================================

# --- code starts from here ---

# BeautifulSoap

import requests
from bs4 import BeautifulSoup

html = "<h1>Hello World</h1><p class='intro'>Python is awesome</p>"

soup = BeautifulSoup(html, "html.parser")

print(soup.h1.text)
print(soup.p.text)
print(soup.p["class"])


# requests + bs4 Combo


url = "https://example.com"
response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)


# find() & findall()

soup.find("h1")
soup.find("p", class_="intro")
soup.find("div", id="main")
soup.find("a", href=True)
soup.find_all("p")
soup.find_all("a")
soup.find_all("li", class_="item")
soup.find_all(["h1", "h2", "h3"])
soup.find_all("p", limit=3)

url = "https://quotes.toscrape.com"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

# Find all quotes
quotes = soup.find_all("span", class_="text")

for quote in quotes:
    print(quote.text)


# extract books title & price

url = "https://books.toscrape.com"
response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    print(f"{title} - {price}")
