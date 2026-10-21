import random

adventures = [
    "You discover a hidden library beneath an old bookstore.",
    "A stranger gives you a map with tomorrow's date on it.",
    "You find a door in a mountain that wasn't there yesterday.",
    "A mysterious letter arrives from your future self.",
    "You wake up on a train with no memory of boarding it.",
]

name = input("What is your name, adventurer? ")
print(f"\nYour adventure begins, {name}...\n")
print(random.choice(adventures))
print()
