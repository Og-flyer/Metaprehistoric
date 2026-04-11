import random
import json
import datetime
import hashlib
import requests

def loadDATA():
    with open("data.json") as f:
        data = json.load(f)
    return data

def locate_Answer():
    creatures = loadDATA()
    chosen = random.choice(creatures)
    return chosen

def locate_Daily_Answer():
    creatures = loadDATA()
    today = str(datetime.date.today())
    hash_val = int(hashlib.md5(today.encode()).hexdigest(), 16)
    return creatures[hash_val % len(creatures)]

def find_creature(name):
    creatures = loadDATA()
    for creature in creatures:
        if creature["name"].lower() == name.lower():
            return creature
    return None

def get_wiki_image(wiki):
    try:
        title = wiki.split("/wiki/")[-1]
        api = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
        headers = {"User-Agent": "Metaprehistoric/1.0"}
        response = requests.get(api, headers=headers)
        data = response.json()
        return data.get("thumbnail", {}).get("source", None)
    except Exception as e:
        print(f"Error: {e}")
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
        if guess == Daily_chosen["name"].lower():
            print("You won!")
            print("Here:")
            for i in Daily_chosen_DATA:
                if i == "name":
                    continue
                print(Daily_chosen_DATA[i]["value"])
            win = True
        else:
            for i in Daily_chosen_DATA:
                if i == "name":
                    continue
                elif guess_DATA[i] == Daily_chosen_DATA[i]:
                    print(Daily_chosen_DATA[i]["value"])
                else:
                    pass
            
