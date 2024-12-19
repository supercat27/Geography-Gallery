
import subprocess

def menu():

    welcome = "Welcome to Geography Gallery! Choose from the many gamemodes listed below to begin!"
    print(welcome)
    seperation = len(welcome)
    print("-"*seperation)

    gamemodes = {
        "1": ("European Countries", european_countries),
        "2": ("European Capitals", european_capitals),
        "3": ("North American Countries", northamerican_countries),
        "4": ("North American Capitals", northamerican_capitals),
        "5": ("Exit Game", exit_game)
    }


    while True:
        for number, (gamemode, _) in gamemodes.items():
            print(f"[{number}] {gamemode}")

        choice = input("Please select a gamemode: ")

        if choice in gamemodes:
            _, action = gamemodes[choice]
            action()
            if choice == "5":
                break
        else:
            print("Invalid gamemode, please try again.")

    
def european_countries():
    print("You selected European Countries!")

def european_capitals():
    print("You selected European Capitals!")
    subprocess.call(["python", "Europe/europe_capitals.py"])

def northamerican_countries():
    print("You selected North American Countries!")

def northamerican_capitals():
    print("You selected North American Capitals!")

def exit_game():
    print("Exiting...")

menu()