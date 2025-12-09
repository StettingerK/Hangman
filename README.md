Darstellungsschicht:
  eingabe_Spieler() -> list
  hangman_zeichnen(hangman_list:list[dict], i:int)
  wort_darstellen(ausgabe:str)
  buchstaben_raten() -> str
Logikschicht:
  main()
  buchstabe_pruefen(wort:str, buchstabe:str) -> bool
  wort_pruefen(wort:str, pruef_wort:str) -> bool
  

Datenschicht:
  wort_erzeugen() -> str
  hangman_vorlage() -> list[dict]
  
