import random
import json

def wort_erzeugen() -> str:
    with open("woerter.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
    woerter:list = []
    for line in data:
        line_woerter = line.split(",")
        for wort in line_woerter:
            woerter.append(wort.upper())
    
    r = random.randint(0,len(woerter))
    return woerter[r]

def hangman_vorlage() -> list[dict]:
    with open("hangman.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    # for line in data: # zum test
    #     for a in line["graphic"]:
    #         print(a)
    return data

if __name__ == "__main__":
    wort_erzeugen()
    hangman_vorlage()