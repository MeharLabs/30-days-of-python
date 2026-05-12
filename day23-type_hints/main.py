# ============================================
# 🐍 Day 23 - Type Hints
# 📅 Date: 12/05/2026
# 🎯 Goal: Understand and apply Python Type Hints from annotations to types and learn how mypy catches bugs before runtime to write safer, cleaner, and more maintainable code.
# =============================================

# --- code starts from here ---


# type hints

from typing import Dict, List, Optional


age: int = 25
name: str = "Ali"
is_active: bool = True
price: float = 9.99


def add(a: int, b: int) -> int:
    return a + b


def is_even(n: int) -> bool:
    return n % 2 == 0


def get_username(user_id: int) -> str:
    return f"user_{user_id}"


type User = dict[str, str | int | None]


def create_user(first_name: str, last_name: str, age: int | None = None) -> User:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
    }


user1 = create_user("Emily", "Whatson", age=34)
user2 = create_user("John", "Doe")

print(user1)
print(user2)

# list


def get_scores(names: List[str]) -> List[int]:
    return [len(name) for name in names]


scores: List[int] = [90, 85, 100]

# dict

user: Dict[str, int] = {"Ali": 25, "Sara": 30}


def word_count(text: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


# function return types
def log_message(msg: str) -> None:
    print(f"[LOG]: {msg}")

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: int, b: int) -> Optional[float]:
    if b == 0:
        return None
    return a / b

def repeat(word: str, times: int) -> List[str]:
    return [word] * times