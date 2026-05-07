# 🌐 Day 18 — API Responses in Python

## 🎯 Goal

API Responses in Python — use the `requests` library to send GET and POST requests, handle response status codes, parse JSON data with `.json()`, and work with query parameters and headers to effectively communicate with web APIs.


## 📌 What is an API Response?

When your Python code sends a request to an API (like asking a server for data), the server sends back an **API Response** — a structured reply containing:

- ✅ A **status code** (did it work?)
- 📦 **Data** (the actual content, usually JSON)
- 📋 **Headers** (metadata about the response)
- 🔗 **URL info** (what was requested)

> 🍕 Think of it like ordering food — you place an order (request), and the restaurant sends back your food + a receipt (response).

---

## 📦 The `requests` Library

The `requests` library is Python's most popular tool for making HTTP calls. It's **not built-in**, so install it first:

```bash
pip install requests
```

```python
import requests  # That's it — you're ready to talk to APIs!
```

> 💡 **Tip:** Always import `requests` at the top of your file. It handles all the complex HTTP stuff so you don't have to!

---

## 🔵 GET Request — *"Give me data"*

A **GET** request *fetches* data from a server. It's read-only — you're just asking, not changing anything.

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)   # 200
print(response.json())        # {'userId': 1, 'id': 1, 'title': '...', 'body': '...'}
```

### 🔍 What you get back:

| Attribute | What it does |
|---|---|
| `response.status_code` | The HTTP status number (200, 404, etc.) |
| `response.json()` | Parses response body as Python dict |
| `response.text` | Raw response as a string |
| `response.content` | Raw bytes (for images/files) |
| `response.headers` | Response headers as a dict |
| `response.url` | The final URL that was requested |
| `response.ok` | `True` if status code < 400 |
| `response.elapsed` | How long the request took ⏱️ |
| `response.encoding` | Text encoding (e.g., `utf-8`) |
| `response.cookies` | Cookies returned by server 🍪 |

---

## 🟢 POST Request — *"Send data to server"*

A **POST** request *sends* data — like submitting a form, creating a user, or logging in.

```python
import requests

payload = {
    "title": "My Post",
    "body": "Hello World!",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload   # ✅ Automatically sets Content-Type: application/json
)

print(response.status_code)  # 201 Created
print(response.json())       # Returns the created object
```

> ⚠️ **Tip:** Use `json=payload` (not `data=payload`) when sending JSON — it auto-sets the correct headers!

---

## 🔢 Response Status Codes

Status codes tell you **what happened** with your request.

### 📊 Status Code Categories:

| Range | Meaning | Emoji |
|---|---|---|
| `1xx` | Informational | 💬 |
| `2xx` | Success | ✅ |
| `3xx` | Redirection | 🔀 |
| `4xx` | Client Error (your fault) | ❌ |
| `5xx` | Server Error (their fault) | 💥 |

### 🔑 Most Common Codes:

| Code | Name | Meaning |
|---|---|---|
| `200` | OK | Everything worked perfectly ✅ |
| `201` | Created | New resource was created 🆕 |
| `204` | No Content | Success but no data returned |
| `301` | Moved Permanently | URL changed forever 🔀 |
| `400` | Bad Request | You sent bad data ❌ |
| `401` | Unauthorized | Login required 🔐 |
| `403` | Forbidden | You don't have permission 🚫 |
| `404` | Not Found | Resource doesn't exist 👻 |
| `429` | Too Many Requests | Slow down! Rate limited ⏳ |
| `500` | Internal Server Error | Server crashed 💥 |
| `503` | Service Unavailable | Server is down 🔧 |

```python
# ✅ Best Practice — Always check before using data
if response.status_code == 200:
    data = response.json()
elif response.status_code == 404:
    print("❌ Not Found!")
elif response.status_code == 401:
    print("🔐 Unauthorized — check your API key!")
else:
    print(f"⚠️ Unexpected: {response.status_code}")

# 🚀 Shortcut — raise an exception for bad codes
response.raise_for_status()  # Raises HTTPError if 4xx or 5xx
```

---

## 🧩 `.json()` Parsing

Most modern APIs return data in **JSON format**. The `.json()` method converts it directly into a Python **dict or list**.

```python
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
data = response.json()

print(data["name"])             # "Leanne Graham"
print(data["email"])            # "Sincere@april.biz"
print(data["address"]["city"])  # Nested access!
```

### 🔄 JSON → Python Type Mapping:

| JSON | Python |
|---|---|
| `object {}` | `dict` |
| `array []` | `list` |
| `string ""` | `str` |
| `number` | `int` / `float` |
| `true/false` | `True` / `False` |
| `null` | `None` |

```python
# 📋 Handling a list response
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()  # Returns a list of dicts

for post in posts[:3]:
    print(f"📝 {post['id']}: {post['title']}")
```

```python
# ⚠️ Always wrap in try/except
try:
    data = response.json()
except ValueError:
    print("⚠️ Response is not valid JSON!")
    print(response.text)
```

---

## 🔍 Query Parameters

Query params are **key=value pairs** added to the URL after `?` — used for filtering, searching, pagination.

```
https://api.example.com/posts?userId=1&limit=5
                                ^^^^^^^^^^^^^^
                                Query parameters
```

```python
# ✅ Use the params argument — clean and safe!
params = {
    "userId": 1,
    "_limit": 3,
    "_sort": "id"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

print(response.url)
# https://jsonplaceholder.typicode.com/posts?userId=1&_limit=3&_sort=id
```

> 💡 `requests` handles **URL encoding** automatically — spaces become `%20`, special chars are escaped. Never do this manually!

---

## 📋 Headers

Headers pass **metadata** with your request — authentication, content type, client info, etc.

```python
headers = {
    "Authorization": "Bearer YOUR_API_TOKEN_HERE",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "MyApp/1.0"
}

response = requests.get(
    "https://api.example.com/protected-data",
    headers=headers
)
```

### 🔑 Common Headers You'll Use:

| Header | Purpose |
|---|---|
| `Authorization` | Send API keys or tokens 🔐 |
| `Content-Type` | Format of data you're sending |
| `Accept` | Format you want back |
| `User-Agent` | Identify your app |
| `X-API-Key` | Alternative API key header |

```python
# 🔍 Reading response headers
print(response.headers["Content-Type"])
print(response.headers.get("X-RateLimit-Remaining"))
```

---

## 🛠️ Other HTTP Methods

```python
# 🔵 GET — Read data
requests.get(url)

# 🟢 POST — Create new data
requests.post(url, json=data)

# 🟡 PUT — Replace entire resource
requests.put(url, json=updated_data)

# 🟠 PATCH — Update part of a resource
requests.patch(url, json={"title": "New Title Only"})

# 🔴 DELETE — Remove a resource
requests.delete(url)
```

---

## ⚙️ Useful `requests` Features

### ⏱️ Timeouts — Never hang forever!
```python
response = requests.get("https://api.example.com", timeout=5)
response = requests.get("https://api.example.com", timeout=(3, 10))  # (connect, read)
```

### 🔁 Sessions — Reuse connections & headers
```python
session = requests.Session()
session.headers.update({"Authorization": "Bearer TOKEN"})

r1 = session.get("https://api.example.com/users")
r2 = session.get("https://api.example.com/posts")
# Headers sent automatically on both! ✅
```

### 🔒 Authentication Built-in
```python
# Basic Auth
response = requests.get(url, auth=("username", "password"))

# Token Auth
response = requests.get(url, headers={"Authorization": "Bearer token123"})
```

---

## 🏆 Tips & Tricks

> 💡 **Always set `timeout`** — without it, your code can hang forever if the server stops responding.

> 🔐 **Never hardcode API keys** — use environment variables: `os.environ.get("API_KEY")`

> 🧪 **Test with JSONPlaceholder** — `https://jsonplaceholder.typicode.com` is a free fake API, perfect for practice!

> ♻️ **Use `Session()`** for multiple requests — it's faster (reuses TCP connections) and cleaner.

> 🚨 **Use `raise_for_status()`** — it automatically throws an error for bad responses so you don't silently fail.

> 📖 **Check `response.text` on errors** — APIs often send helpful error messages in the body even on 4xx/5xx.

> 🧩 **Use `.get()` on dicts** — `data.get("key", "default")` is safer than `data["key"]` which crashes if missing.

---

## 🧪 Full Practical Example

```python
import requests
import os

API_KEY = os.environ.get("MY_API_KEY")  # 🔐 Never hardcode!
BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_user_posts(user_id: int, limit: int = 5):
    """Fetch posts for a specific user."""

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    params = {
        "userId": user_id,
        "_limit": limit
    }

    try:
        response = requests.get(
            f"{BASE_URL}/posts",
            headers=headers,
            params=params,
            timeout=5
        )

        response.raise_for_status()

        posts = response.json()
        print(f"✅ Found {len(posts)} posts for user {user_id}")

        for post in posts:
            print(f"  📝 [{post['id']}] {post['title']}")

        return posts

    except requests.exceptions.Timeout:
        print("⏱️ Request timed out!")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("🌐 Connection failed — check your internet!")
    except ValueError:
        print("⚠️ Could not parse JSON response!")

# Run it!
fetch_user_posts(user_id=1, limit=3)
```

---

## 🗺️ Quick Reference Cheatsheet

```python
import requests

r = requests.get(url, params={}, headers={}, timeout=5)
r = requests.post(url, json={}, headers={}, timeout=5)

r.status_code         # 200, 404, 500...
r.ok                  # True if < 400
r.json()              # dict or list
r.text                # raw string
r.headers             # response headers dict
r.url                 # final URL
r.elapsed             # response time
r.raise_for_status()  # throw on error
```

---

## 📚 What I Learned

- 🌐 **What an API Response is** - the structured reply a server sends back after you make a request, containing status codes, data, and headers
- 📦 **The `requests` library** - how to install and use Python's most popular HTTP library to communicate with APIs
- 🔵 **GET Requests** - how to fetch/read data from an API endpoint using `requests.get()`
- 🟢 **POST Requests** - how to send/create data to a server using `requests.post()` with a JSON payload
- 🔢 **Response Status Codes** - what 200, 201, 404, 401, 500 etc. mean and how to handle them properly
- 🧩 **`.json()` Parsing** - how to convert API response data into Python dictionaries and lists
- 🔍 **Query Parameters** - how to filter and customize requests using the `params={}` argument cleanly
- 📋 **Headers** - how to send metadata like API keys and content types using `headers={}`
- ⚙️ **Other HTTP Methods** - the purpose of PUT, PATCH, and DELETE beyond just GET and POST
- ⏱️ **Timeouts & Sessions** - best practices like always setting a timeout and reusing sessions for multiple requests
- 🏆 **Tips & Tricks** — never hardcode API keys, always use `raise_for_status()`, and test with JSONPlaceholder


## 🎯 Key Takeaways

- 🌐 **APIs communicate through requests & responses** - you ask, the server answers, and everything flows through HTTP
- 📦 **`requests` is your best friend** - one simple library handles all the complexity of HTTP communication in Python
- 🔢 **Status codes tell the whole story** - always check them first before touching the response data, `2xx` is good, `4xx` is your mistake, `5xx` is their problem
- 🧩 **`.json()` bridges API and Python** - it instantly converts raw JSON into native Python dicts and lists you can work with directly
- 🔍 **Never build URLs manually** - always use `params={}` and let `requests` handle encoding cleanly and safely
- 🔐 **Security starts with headers** - API keys and tokens always go in headers, never in the URL or hardcoded in your code
- ⏱️ **Always set a timeout** - one missing `timeout=5` can freeze your entire program indefinitely
- 🚨 **`raise_for_status()` is a must** - it prevents you from silently processing failed responses as if they succeeded
- ♻️ **Use `Session()` for efficiency** - it reuses connections and headers automatically, making multiple requests faster and cleaner
- 🛡️ **Always handle exceptions** - network calls can fail anytime, wrapping in `try/except` is not optional, it's professional practice