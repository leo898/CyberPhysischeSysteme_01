"""
Alles run um den Bezahlvorgang.
"""
from utils import euro_formater, ask_yes_no
from config import ACCEPTED_COINS

def payment_process(price: float) -> tuple[bool, float]:
    """
    Bezahlvorgang des Kaffeeautomats.
    
    Ablauf:
    - Der Benutzer wirft Münzen
    - Nach jeder Münze wird geprüft, ob der Preis erreicht ist.
    - Ist noch zu wenig bezahlt, darf der Benutzer entscheiden, ob er
      weiterzahlen oder abbrechen möchte.
    - Bei Abbruch wird das gesamte eingeworfene Geld zurückgegeben.
    
    Rückgabwert:
    - True -> Zahlung erfolgreich abgeschlossen
    - False -> Zahlung abgebrochen
    - Zweiter Wert: Insgesamt eingeworfener Geldbetrag
    """
    # Wie viel Geld hat der Benutzer, bisher eingeworfen:
    inserted = 0.0
    
    # Anzeige des zu zahlenden Preises:
    print(f"\nPreis: {euro_formater(price)}")
    print("Bitte Münzen einwerfen.")
    print(f"Erlaubte Münzen: {', '.join(euro_formater(c) for c in ACCEPTED_COINS)}")
    
    # Schleife bis genug bezahl wurde oder der Benutzer abbricht:
    while True:
        # Berechnung des noch offenen Betrags:
        remaining = price - inserted
        
        # Solange nicht genug bezahlt, offenen Betrag anzeigen:
        if remaining > 0:
            print(f"Noch offen: {euro_formater(remaining)}")
        
        # Eingabe der Münzen:
        coin_str = input("Münnze eingeben (z.B. 0.50) oder 'cancel': ").strip().lower()
        
        # Sonderfall: Benutzer bricht Bezahlvorgang ab:
        if coin_str == "cancel":
            print(f"Abbruch. Geld wird zurückgegeben: {euro_formater(inserted)}\n")
            return False, inserted
        
        # Datentypkonvertierung und erlaubt Punk oder Komma als Dezimaltrenner:
        try:
            coin = float(coin_str. replace(",", "."))
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Münze (z.B. 0.50) oder 'cancel' eingeben")
            continue
        
        # Rundung auf zwei Nachkommastellen:
        coin = round(coin, 2)
        
        # Prüfen, ob Münze akzeptiert wird:
        if coin not in ACCEPTED_COINS:
            print("Diese Münze wird nicht akzeptiert.")
            continue
        
        # Eingeworfenen Geldbetrag erhöhen:
        inserted = round(inserted + coin, 2)
        
        # Prüfen ob genug Geld eingeworfen wurde:
        if inserted < price:
            if not ask_yes_no("Noch nicht genug bezahlt. Weiterzahlen? (ja/nein): "):
                # Benutzer möchte nicht weiterzahlen:
                print(f"Geld wird zurückgegeben: {euro_formater(inserted)}\n")
                return False, inserted
        else:
            return True, inserted