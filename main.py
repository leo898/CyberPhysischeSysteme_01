from config import resources, MENU, ACCEPTED_COINS
from utils import euro_formater, ask_yes_no

# ---------------------
# Hilfsfunktionen
# ---------------------
def report() -> None:
    """Gibt den aktuellen Status des Automaten aus."""
    print("\n--- REPORT ---")
    print(f"Wasser: {resources['water_ml']} ml")
    print(f"Milch: {resources['milk_ml']} ml")
    print(f"Kaffee: {resources['coffee_g']} g")
    print(f"Geld: {euro_formater(amount=resources['money_eur'])}")
    print("-----------\n")

# Tuple Beispiel: (True, [Milch, Apfel...])
# Tuple Beispiel: (True, "Gandalf")
def ingredients_ok(drink_key: str) -> tuple[bool, list[str]]:
    """
    Prüft, ob genug Zutaten für das Getränk vorhanden sind.
    Rückgabe:
    - (True, []) wenn alles vorhanden ist
    - (False, [liste_der_fehlenden_zutaten]) wenn etwas fehlt
    """
    missing_ingredients = []
    needs = MENU[drink_key]["needs"] # In "needs" ist {'water_ml': 50, 'milk_ml': 100, 'coffee_g': 15}
    for ing, amount_needed in needs.items():
        if resources[ing] < amount_needed:
            pretty = ing.replace("_ml", "").replace("_g", "")
            missing_ingredients.append(pretty)
    
    if missing_ingredients:
        return False, missing_ingredients
    return True, []

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
        
def handle_change_and_profit(price: float, inserted: float) -> float:
    """
    Berechnet das Wechselgeld und bucht die Einnahmen.
    """
    
    # Wechselgeld:
    change = round(inserted - price, 2)
    
    # Einnahmen verbuchen:
    resources["money_eur"] = round(resources["money_eur"] + price, 2)
    
    # Ausgaben für den Benutzer:
    if change > 0:
        print(f"Wechselgeld notwendig: ja")
        print(f"Rückgabe Wechselgeld: {euro_formater(change)}")
    else:
        print("Wechselgeld notwendig: Nein")
    return change

def make_drink(drink_key: str) -> None:
    """
    Simuliert die Zubereitung des Getränks.
    """
    
    print("\nGetränk wird zubereitet...")
    print(f"{drink_key.capitalize()} ist fertig. ☕")
    print("Bitte entnehmen.\n")
    
def deduct_ingredients(drink_key: str) -> None:
    """
    Zieht die Zutaten für das gewählte Getränk ab.
    """
    needs = MENU[drink_key]["needs"]
    
    # Für jede Zutat die benötigt wird, ziehen wir die Menge von Ressourcen ab:
    for ing, amount_needed in needs.items():
        resources[ing] -= amount_needed # resources[ing] = resources[ing] - amount_needed
    
# ---------------------
# Hauptprogramm
# ---------------------
def main():
    while True:
        print("=== Kaffeeautomat ===")
        print("Unsere Getränke: Espresso | Latte | Cappuccino\n")
        
        choice = input("Getränk auswählen: ").lower().strip()
        if choice == "off":
            print("Automat wird ausgeschaltet")
            break
        if choice == "report":
            report()
            continue
        if choice not in MENU:
            print("Ungültige Auswahl. Bitte 'Espresso', 'Latte' oder 'Cappuccino' eingeben.\n")
            
        ok, missing = ingredients_ok(choice)
        if not ok:
            print("Folgende Zutaten fehlen für dieses Getränk:")
            for ingredient in missing:
                print(f"- {ingredient}")
            print()
            continue
    
        price = MENU[choice]["price"]
        print(f"\nDu hast gewählt: {choice.capitalize()}")
        print(f"Zu bezahlen: {euro_formater(price)}\n")
        
        paid, inserted = payment_process(price)
        if not paid:
            continue
        
        handle_change_and_profit(price, inserted)
        
        make_drink(choice)
        
        deduct_ingredients(choice)
        print("Zutaten wurden aktualisiert. Zurück zur Startsituation...\n")

if __name__ == "__main__":
    main()