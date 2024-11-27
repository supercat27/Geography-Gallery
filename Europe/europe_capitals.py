import time
import random
import json
import subprocess
import tkinter

with open("Europe/european_countries_and_capitals.json") as json_file:
    capitals = json.load(json_file)
    c = capitals



t = 15
limit = range(t, -1, -1)

def countdown(t):
    for t in limit:
        time.sleep(1)
        print(f"\r{' ' * 20}", end="")
        print(f"\rTime left: {t}", end="")
            




print("Welcome to the European Capitals quiz!")
time.sleep(0.75)
print("A European country will be shown and you will need to guess it's capital.")
time.sleep(0.75)
play = input("Ready? (y/n) ")







def quiz(c):
    q = input("How many questions would you like?\n")
    wrong = 0
    right = 0
    for i in range(int(q)):
        country, capital = random.choice(list(c.items()))
        ans = input(f"What is the capital city of {country}?\n")
        ans = ans.lower()


        if ans == capital.lower():
            right += 1
            print(f"Correct! The capital city of {country} is {capital}!")
        else:
            wrong += 1
            print(f"Wrong! The capital city of {country} is {capital}!")
    print(f"You got {wrong} wrong, and {right} right!")

        





if play == "y":
    time.sleep(0.75)
    quiz(c)
elif play == "n":
    print("Goodbye!")
    time.sleep(2)
    subprocess.call(["python", "menu.py"])









