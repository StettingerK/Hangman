import random

def wort_erzeugen() -> str:
    with open("woerter.txt", "r") as file:
        data = file.readlines()
    woerter:list = []
    for line in data:
        line_woerter = line.split(",")
        for wort in line_woerter:
            woerter.append(wort.upper())
    
    r = random.randint(0,len(woerter))
    return woerter[r]

def hangman_vorlage() -> list[dict]:
    pass

if __name__ == "__main__":
    wort_erzeugen()