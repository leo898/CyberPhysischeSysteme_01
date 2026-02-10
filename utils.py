"""
Kleine Hilfsfunktionen, die überall gebraucht werden können.
"""

def euro_formater(amount: float) -> str:
    """Schöne Euro-Ausgabe"""
    # 35.50 -> 35,50 €
    # 24.2425 -> 24,24 €
    return f"{amount:.2f}".replace(".", ",") + " €"

def ask_yes_no(prompt: str) -> bool:
    """
    Fragt den Benutzer nach ja/nein.
    Gibt 'True' für ja zurück.
    """
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("ja", "j", "yes", "y"):
            return True
        if answer in ("nein", "n", "no"):
            return False
        print("Bitte mit 'ja' oder 'nein' antworten.")