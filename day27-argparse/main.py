# ============================================
# 🐍 Day 27 - Argparse CLI
# 📅 Date: 18/05/2026
# 🎯 Goal: how to use Python's argparse module to build CLI tools that accept and validate arguments from the terminal.
# =============================================

# --- code starts from here ---

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("greeting", help="The greeting message displayed")
parser.add_argument('-n', '--numbers', type=float, nargs='*',
                    help='The numbers to be added')
parser.add_argument('-v', '--verbosity', type=int, choices=[0, 1, 2],
                    help='Determine how much choice do you have')

args = parser.parse_args()

print(args)

print(args.numbers)

if args.verbosity is None:
    print(args.greeting)
    if args.number is not None:
        print(sum(args.numbers))

else:
    if args.verbosity >= 0:
        print(args.greeting)
        if args.number is not None:
            print(sum(args.numbers))
    if args.verbosity >= 1:
        print(args.numbers)
    if args.verbosity == 2:
        print("Extra info")
