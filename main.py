import darstellungsschicht
import datenschicht
import os

def buchstabe_pruefen(hiden_wort:str, visible_wort, buchstabe:str) -> str:    
    for zeichen in range(0,len(visible_wort)):
        if hiden_wort[zeichen] == buchstabe:
            visible_wort = visible_wort[0:zeichen] + buchstabe + visible_wort[zeichen+1:]
    return visible_wort

def wort_pruefen(wort:str, pruef_wort:str) -> bool:
    if wort == pruef_wort:
        return True
    else:
        return False 

def pruefer_gewonnen(hiden_wort:str, visible_wort:str) -> bool:
    new_visible_wort = ""
    for i in range(0,len(visible_wort)):
        if visible_wort[i] != " ":
            new_visible_wort += visible_wort[i]
    return wort_pruefen(new_visible_wort,hiden_wort)
        


def main():
    spieler:list = darstellungsschicht.eingabe_spieler()
    hiden_wort:str = datenschicht.wort_erzeugen()
    visible_wort:str = "".join("_" for count in range(0,len(hiden_wort)))
    hangman_vorlage:list[dict] = datenschicht.hangman_vorlage()
    game_running:bool = True
    falsche_buchstaben = []
    spieler_count = 0
    wrong_guesses = 0
    while game_running:
        os.system("cls" if os.name == "nt" else "clear") # clear terminal
        # Spieler an der reihe
        print(f"{spieler[spieler_count]} ist dran")
        spieler_count = spieler_count +1 if spieler_count < len(spieler)-1 else 0 # spieler_count hochzählen sonst zurücksetzen
        
        # Hangman zeichnen mit flaschen Buchstaben darstellen
        darstellungsschicht.hangman_zeichnen(hangman_vorlage,wrong_guesses)
        if len(falsche_buchstaben) > 0:
            print("Falsche Buchstaben: " + ", ".join(falsche_buchstaben))
        darstellungsschicht.wort_darstellen("".join(zeichen +" " for zeichen in visible_wort))

        # Buchstaben Überprüfen und verändern
        buchstabe = darstellungsschicht.buchstaben_raten()
        if len(buchstabe) == 1: # überprüfe ob Buchstabe oder Wort eingegeben
            # Wenn Buchstabe eingegeben
            new_visible_wort = buchstabe_pruefen(hiden_wort,visible_wort,buchstabe)
            if new_visible_wort != visible_wort:
                visible_wort = new_visible_wort
            else:
                falsche_buchstaben.append(buchstabe)
                wrong_guesses += 1
        else: 
            # Wenn Wort eingegeben
            if wort_pruefen(hiden_wort,buchstabe):
                print(f"\nDu hast gewonnen\nDas Wort war: {hiden_wort}")
                game_running = False
            else:
                wrong_guesses += 1
        if pruefer_gewonnen(hiden_wort,visible_wort):
            print(f"\nDu hast gewonnen\nDas Wort war: {hiden_wort}")
            game_running = False

if __name__ == "__main__":
    main()