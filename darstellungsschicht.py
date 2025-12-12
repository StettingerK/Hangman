import datenschicht

def eingabe_spieler() -> list:
    spieler = []
    while True:
        try:
            anzahl_spieler = int(input("Geben Sie die Anzahl der Mitspieler ein: "))
            for i in range(anzahl_spieler):
                name_spieler = input(f"Geben Sie den Namen für Spieler {i+1} ein: ")
                spieler.append(name_spieler)
        except ValueError:
            (print("Geben Sie eine gültige Anzahl ein!"))
            continue
        return spieler

def hangman_zeichnen(hangman_list:list[dict], i:int):
    for stage in hangman_list:
      if stage["stage"] == i:
        for a in stage["graphic"]:
            print(a)

def wort_darstellen(ausgabe:str):
    print(f"\n{ausgabe}")

def buchstaben_raten() -> str:
    pass

if __name__ == "__main__":
    #eingabe_spieler()
    hangman_zeichnen(datenschicht.hangman_vorlage(), 3)