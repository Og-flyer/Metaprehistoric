import random
import json

def loadDATA():
    with open("data.json") as f:
        data = json.load(f)
    return data

def locate_Answer():
    creatures = loadDATA()
    chosen = random.choice(creatures)
    return chosen

def find_creature(name):
    creatures = loadDATA()
    for creature in creatures:
        if creature["name"].lower() == name.lower():
            return creature
    return None

def gameplay():
    Daily_chosen = locate_Answer()
    win = False
    while win == False:
        guess = input("write the guess: ")
        guess_DATA = find_creature(guess)
        if guess_DATA is None:
            print("please write another thing!")
            continue
        Daily_chosen_DATA = Daily_chosen
        if guess == Daily_chosen["name"]:
            print("You won!")
            print("Here:")
            for i in Daily_chosen_DATA:
                print(Daily_chosen_DATA[i])
            win = True
        else:
            for i in Daily_chosen_DATA:
                if i == "name":
                    continue
                elif guess_DATA[i] == Daily_chosen_DATA[i]:
                    print(Daily_chosen_DATA[i])
                else:
                    pass
            
