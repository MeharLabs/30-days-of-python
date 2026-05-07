# 🟢 Level 1 — Easy (just getting started)
# =======================================

# Q1. Fetch a list of all users** from "https://jsonplaceholder.typicode.com/users" and print only their name and email.

import requests

base_url = "https://jsonplaceholder.typicode.com/users"


def get_user_names():
    response = requests.get(base_url)

    if response.status_code == 200:
        user_data = response.json()

        for user in user_data:
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print("-" * 30)
    else:
        print(f"Failed to retrieve data {response.status_code}")


get_user_names()

# Q2. **Send a POST request** to `https://jsonplaceholder.typicode.com/posts` with a title, body, and userId — print the response status code and returned data.


base_url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Hello from Python",
    "body": "This is test post",
    "userId": 1,
}

response = requests.post(base_url, json=payload)

print("Status Code: ", response.status_code)

if response.status_code == 201:
    print("Post created successfully")
    print(response.json())
else:
    print("Request failed")

# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# Q3. Use query params to fetch only posts where "userId=3" from "/posts" and count how many there are.

base_url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 3}

response = requests.get(base_url, params=params)
print("Final URL: ", response.url)

response.raise_for_status()

data = response.json()

count = len(data)
print("Total Posts:", count)

for post in data:
    print("Title: ", post["title"])


# Q4. Handle errors gracefully - make a request to a fake endpoint like /notreal and handle the 404 properly without crashing.


base_url = "https://jsonplaceholder.typicode.com/notreal"

try:
    response = requests.get(base_url)

    response.raise_for_status()

    data = response.json()
    print(data)
except requests.exceptions.HTTPError as error:
    print(f"HTTP Error Occurred: {error}")

except requests.exceptions.RequestException as error:
    print(f"Request Failed: {error}")


# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================

# Q5. Check response time - fetch any endpoint and print how long the request took using response.elapsed.


base_url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(base_url)

print("Status Code:", response.status_code)

print(f"Response Time: {response.elapsed.total_seconds():.2f} seconds")
