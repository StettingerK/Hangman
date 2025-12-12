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
    erlaubte_buchstaben = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß"

    while True:
        guess = input("Geben Sie einen Buchstaben oder das gesuchte Wort ein: ").strip().upper()

        #Leere Eingabe verhindern
        if not guess:
            print("Eingabe darf nicht leer sein!")
            continue

        #Prüfen, ob NUR erlaubte Buchstaben enthalten sind
        for buchstabe in guess:
            if buchstabe not in erlaubte_buchstaben:
                print("Bitte nur Buchstaben (A-Z, Ä, Ö, Ü, ß) eingeben!")
                break
        else:
            return guess

def print_line():
    print("-"*40)

#if __name__ == "__main__":
    #eingabe_spieler()
    #hangman_zeichnen(datenschicht.hangman_vorlage(), 3)
    #buchstaben_raten()