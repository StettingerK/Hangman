import darstellungsschicht
import datenschicht
import os

def check_char(hiden_word:str, visible_word, buchstabe:str) -> str:    
    for zeichen in range(0,len(visible_word)):
        if hiden_word[zeichen] == buchstabe:
            visible_word = visible_word[0:zeichen] + buchstabe + visible_word[zeichen+1:]
    return visible_word

def check_word(word:str, check_word:str) -> bool:
    if word == check_word:
        return True
    else:
        return False 

def check_won(hiden_word:str, visible_wort:str) -> bool:
    new_visible_wort = ""
    for i in range(0,len(visible_wort)):
        if visible_wort[i] != " ":
            new_visible_wort += visible_wort[i]
    return check_word(new_visible_wort,hiden_word)
        


def main():
    spieler:list = darstellungsschicht.eingabe_spieler()
    hiden_word:str = datenschicht.wort_erzeugen()
    visible_word:str = "".join("_" for count in range(0,len(hiden_word)))
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
        darstellungsschicht.wort_darstellen("".join(zeichen +" " for zeichen in visible_word))

        if wrong_guesses == 10:
            print(f"Ihr habt verloren\nDas Wort war: {hiden_word}")
            break
        # Buchstaben Überprüfen und verändern
        buchstabe = darstellungsschicht.buchstaben_raten()
        if len(buchstabe) == 1: # überprüfe ob Buchstabe oder Wort eingegeben
            # Wenn Buchstabe eingegeben
            new_visible_wort = check_char(hiden_word,visible_word,buchstabe)
            if new_visible_wort != visible_word:
                visible_word = new_visible_wort
            else:
                if buchstabe not in falsche_buchstaben:
                    falsche_buchstaben.append(buchstabe)
                wrong_guesses += 1
        else: 
            # Wenn Wort eingegeben
            if check_word(hiden_word,buchstabe):
                print(f"\nDu hast gewonnen\nDas Wort war: {hiden_word}")
                game_running = False
            else:
                wrong_guesses += 1
        if check_won(hiden_word,visible_word):
            print(f"\nDu hast gewonnen\nDas Wort war: {hiden_word}")
            game_running = False

if __name__ == "__main__":
    main()