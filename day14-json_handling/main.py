# ============================================
# 🐍 Day 14 - JSON Handling
# 📅 Date: 28/04/2026
# 🎯 Goal: Master reading, writing, and manipulating JSON data in Python. Converting between strings, dictionaries, and files using json.loads(), json.dumps(), json.load(), and json.dump(), while keeping output clean with pretty printing.
# =============================================

# --- code starts from here ---

# JSON: JavaScript Object Notation

import json, os

json_string = '''
{
    "students": [
        {
            "id": 1,
            "name": "John",
            "age": 24,
            "full-time": true
        },
        {
            "id": 2,
            "name": "Joe",
            "age": 33,
            "full-time": false
        }
    ]
}
'''
# loading JSON string
data = json.loads(json_string)
print(data["students"])

# creating JSON string
data['test'] = True
new_json = json.dumps(data, indent=4, sort_keys=True)
print(new_json)

# reading JSON files
file = "data.json"
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "data.json")

with open(file_path, "r") as f:
    data = json.load(f)

print(data)

# writing JSON to a file

with open("data2.json", "w") as f:
    json.dump(data, f)