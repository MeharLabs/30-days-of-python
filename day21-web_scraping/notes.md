# 🕸️ Day 21 — Web Scraping with Python

## 🎯 Goal

Learn how to automatically extract data from websites using Python's `requests` and `BeautifulSoup` libraries — HTML parsing, element selection, and ethical scraping practices to build real-world data collection tools responsibly.


## 📌 What is Web Scraping?

Web scraping is the **automated process of extracting data from websites**. Instead of manually copying information, you write a program that visits a webpage, reads its HTML structure, and pulls out the data you need — like prices, headlines, links, images, or any text content.

Think of it like a robot 🤖 that reads a webpage and collects specific information for you at lightning speed.


## 🧰 Core Libraries You'll Use

| Library | Purpose |
|---|---|
| `requests` | Fetches the raw HTML of a webpage |
| `BeautifulSoup (bs4)` | Parses and navigates the HTML tree |
| `lxml` | Fast HTML/XML parser (used with bs4) |
| `selenium` | Handles JavaScript-rendered pages |
| `scrapy` | Full scraping framework for large projects |
| `httpx` | Modern async alternative to `requests` |


## 🌸 BeautifulSoup Basics

**BeautifulSoup** is a Python library that makes it easy to extract data from HTML and XML files. It creates a **parse tree** from the raw HTML, which you can then search and navigate.

```python
from bs4 import BeautifulSoup

html = "<h1>Hello World</h1><p class='intro'>Python is awesome</p>"

soup = BeautifulSoup(html, "html.parser")

print(soup.h1.text)        # Hello World
print(soup.p.text)         # Python is awesome
print(soup.p["class"])     # ['intro']
```

### 🔧 Parsers you can use with bs4:

| Parser | Speed | Notes |
|---|---|---|
| `html.parser` | Medium | Built-in, no install needed |
| `lxml` | ⚡ Fast | Needs `pip install lxml` |
| `html5lib` | Slow | Most lenient/accurate |

---

## 🤝 requests + bs4 Combo

This is the **classic duo** for web scraping. `requests` grabs the page, `bs4` parses it.

```python
import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the page
url = "https://example.com"
response = requests.get(url)

# Step 2: Check status
print(response.status_code)  # 200 = OK ✅

# Step 3: Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract the title
print(soup.title.text)
```

### 📦 Adding Headers (to look like a real browser):

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
```

> 💡 Many websites block requests without a User-Agent header. Always add one!


## 🔍 .find() and .find_all()

These are the **two most important methods** in BeautifulSoup.

### 🎯 `.find()` — Returns the FIRST match

```python
soup.find("h1")                            # First <h1> tag
soup.find("p", class_="intro")            # First <p> with class="intro"
soup.find("div", id="main")               # First <div> with id="main"
soup.find("a", href=True)                 # First <a> that has an href
```

### 🎯 `.find_all()` — Returns ALL matches as a list

```python
soup.find_all("p")                         # All <p> tags
soup.find_all("a")                         # All links
soup.find_all("li", class_="item")        # All <li> with class="item"
soup.find_all(["h1", "h2", "h3"])         # Multiple tag types
soup.find_all("p", limit=3)               # Only first 3 results
```

### 🔎 Real Example:

```python
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

# Find all quotes
quotes = soup.find_all("span", class_="text")

for quote in quotes:
    print(quote.text)
```


## 📤 Extracting Text & Links

### 📝 Extracting Text:

```python
tag = soup.find("p")
print(tag.text)                               # Includes whitespace
print(tag.get_text())                         # Same as .text
print(tag.get_text(strip=True))              # ✅ Removes extra whitespace

all_text = soup.get_text(separator="\n", strip=True)  # All page text
```

### 🔗 Extracting Links:

```python
links = soup.find_all("a")

for link in links:
    href = link.get("href")    # .get() is safer than ["href"]
    text = link.get_text(strip=True)
    print(f"Text: {text} → URL: {href}")
```

### 🖼️ Extracting Images:

```python
images = soup.find_all("img")

for img in images:
    src = img.get("src")
    alt = img.get("alt", "No alt text")
    print(f"Image: {src} | Alt: {alt}")
```

### 📊 Extracting Tables:

```python
table = soup.find("table")
rows = table.find_all("tr")

for row in rows:
    cells = row.find_all(["td", "th"])
    data = [cell.get_text(strip=True) for cell in cells]
    print(data)
```

---

## 🧭 Navigation Methods

| Method | What it does |
|---|---|
| `tag.parent` | Goes up to the parent element |
| `tag.children` | Direct children (iterator) |
| `tag.descendants` | All nested children |
| `tag.next_sibling` | Next element at same level |
| `tag.previous_sibling` | Previous element at same level |
| `tag.find_next("tag")` | Next occurrence of a tag |
| `tag.select("css")` | CSS selector support 🎯 |

### 🎨 CSS Selectors with `.select()`:

```python
soup.select("div.container p")         # <p> inside div.container
soup.select("#main > h1")              # <h1> direct child of #main
soup.select("a[href^='https']")        # Links starting with https
soup.select("ul li:first-child")       # First <li> in each <ul>

soup.select_one("h1").text             # Returns single result
```

---

## 💡 Tips & Tricks

### ⚡ Tip 1: Use `timeout` to avoid hanging
```python
response = requests.get(url, timeout=10)
```

### ⚡ Tip 2: Handle errors gracefully
```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

### ⚡ Tip 3: Use `.get()` instead of `[]` on attributes
```python
link["href"]        # ❌ Crashes if href is missing
link.get("href")    # ✅ Returns None safely
```

### ⚡ Tip 4: Scrape multiple pages (pagination)
```python
for page in range(1, 6):
    url = f"https://example.com/page/{page}"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    # ... scrape each page
```

### ⚡ Tip 5: Save scraped data to CSV
```python
import csv

data = [["Title", "Price"], ["Book 1", "$10"], ["Book 2", "$15"]]

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

### ⚡ Tip 6: Add delays to avoid overloading servers
```python
import time

for url in url_list:
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    time.sleep(2)   # Wait 2 seconds between requests 😴
```

---

## ⚖️ Ethical Scraping Rules

> 🚨 Just because you **can** scrape doesn't mean you **should**. Always be responsible!

### ✅ DO's:
- 📄 **Check `robots.txt`** — visit `https://example.com/robots.txt` to see what's allowed
- 🐢 **Rate limit your requests** — don't hammer a server with 1000 requests/second
- 🙋 **Identify yourself** — use a real User-Agent with your contact info
- 📚 **Only scrape public data** — don't bypass logins or paywalls
- 💾 **Cache responses** — don't re-fetch pages you've already scraped

### ❌ DON'Ts:
- 🚫 Don't scrape personal/private data (violates GDPR, privacy laws)
- 🚫 Don't ignore `robots.txt` disallow rules
- 🚫 Don't overload small websites with requests
- 🚫 Don't resell scraped data without permission
- 🚫 Don't scrape and violate a site's Terms of Service

### 🤖 How to check robots.txt:
```python
# Always check: https://targetsite.com/robots.txt
# Example robots.txt:
# User-agent: *
# Disallow: /private/
# Disallow: /admin/
# Crawl-delay: 5       ← Wait 5 seconds between requests
```

---

## 🗺️ Quick Reference Cheat Sheet

```python
import requests
from bs4 import BeautifulSoup

# ── Fetch ──────────────────────────────────
r = requests.get(url, headers=headers, timeout=10)
soup = BeautifulSoup(r.text, "html.parser")

# ── Find ───────────────────────────────────
soup.find("tag")                  # First match
soup.find_all("tag")              # All matches
soup.select("css selector")       # CSS style
soup.select_one("css selector")   # First CSS match

# ── Extract ────────────────────────────────
tag.text                          # Raw text
tag.get_text(strip=True)         # Clean text
tag.get("attr")                   # Safe attribute access
tag["attr"]                       # Direct attribute access

# ── Navigate ───────────────────────────────
tag.parent
tag.children
tag.next_sibling
tag.find_next("tag")
```

---

## 📚 What I Learned

- 🕸️ **Web Scraping** is the automated process of extracting data from websites using Python
- 🌸 **BeautifulSoup** parses raw HTML into a navigable tree structure
- 📦 **requests** library fetches the raw HTML content of any webpage
- 🤝 **requests + bs4 combo** is the classic and most popular scraping duo
- 🎯 **.find()** returns the first matching HTML element
- 🔍 **.find_all()** returns a list of all matching HTML elements
- 🎨 **.select()** allows powerful CSS selector style searching
- 📝 **.get_text()** extracts clean readable text from any HTML tag
- 🔗 **.get("href")** safely extracts links without crashing on missing attributes
- 🖼️ Images, tables, and links can all be extracted with simple loops
- 🧭 Navigation methods like **.parent**, **.children**, **.next_sibling** help move through HTML
- ⚡ Always use **timeout**, **error handling**, and **delays** for robust scraping
- 🤖 Always check **robots.txt** before scraping any website
- ⚖️ **Ethical scraping** means respecting rules, privacy laws, and server limits
- 💾 Scraped data can be saved directly into a **CSV file** for later use

---

## 🏆 Key Takeaways

- 🔑 **requests fetches, BeautifulSoup parses** — these two libraries together are all you need to start scraping any static website
- 🎯 **.find() vs .find_all()** — use `.find()` for one result, `.find_all()` for many — mastering these two unlocks 80% of scraping tasks
- 🛡️ **.get() is safer than []** — always use `tag.get("attr")` to avoid crashes when an attribute is missing
- 🎨 **CSS Selectors are powerful** — `.select()` gives you flexible, precise control just like styling in CSS
- 🐢 **Slow down your scraper** — adding `time.sleep()` between requests protects servers and keeps you from getting blocked
- 🤖 **robots.txt is the law of scraping** — always read it before scraping any website, ignoring it is unethical and sometimes illegal
- 🧹 **Always clean your data** — use `get_text(strip=True)` to remove unwanted whitespace from extracted content
- ⚖️ **Ethics come first** — scraping publicly available data responsibly is fine, but never scrape private data, bypass logins, or violate Terms of Service
- 💾 **Scraped data is only useful when stored** — always export your results to CSV, JSON, or a database
- 🚀 **This is just the beginning** — once you master requests + bs4, you can level up to **Scrapy** for big projects and **Selenium** for JavaScript-heavy websites

---

> 🧠 **Golden Rule:** Web scraping = `requests` to **fetch** + `BeautifulSoup` to **parse** + **ethics** to **stay responsible**. Scrape like a guest, not like an attacker! 🕷️