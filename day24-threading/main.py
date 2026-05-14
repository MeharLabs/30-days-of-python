# ============================================
# 🐍 Day 24 - Threading
# 📅 Date: 13/05/2026
# 🎯 Goal: Multiple tasks concurrently in Python using the threading module - covering how to create, start, and join threads, keep shared data safe with locks, and know when threading actually helps.
# =============================================

# --- code starts from here ---


# syntax
# t = threading.Thread(target=function_name, args=(arg1, arg2))

import threading, time


def greet(name):
    print(f"Hello, {name}! 👋")


t = threading.Thread(target=greet, args=("Alice",))
t.start()


start = time.perf_counter()


def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping...")


do_something()
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")



def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking the {first} {last}")


def take_out_trash():
    time.sleep(2)
    print("You take out the trash")


def get_mail():
    time.sleep(4)
    print("You get the mail")


chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")
