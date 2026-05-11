# ============================================
# 🐍 Day 22 - Testing with Pytest
# 📅 Date: 11/05/2026
# 🎯 Goal: To learn how to write automated tests in Python using pytest - covering why testing matters, how to write test functions with the test_ naming convention, use assert statements to verify code behavior, and run tests from the terminal.
# =============================================

# --- code starts from here ---


def get_weather(temp):
    if temp > 20:
        return "hot"
    else:
        return "cold"


def add(a, b):
    return a+b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b


class UserManager:
    def __init__(self):
        self.user = {}

    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = email
        return True
    
    def get_user(self, username):
        return self.users.get(username)