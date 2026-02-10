from config import MENU, resources
from utils import euro_formater
from payment import payment_process
from machine import report, ingredients_ok, handle_change_and_profit, make_drink, deduct_ingredients
from storage import save_resources, load_resources

def main():
    # Beim Start, letzten Zustand laden (falls vorhanden):
    loaded = load_resources(resources)
    if loaded:
        print("Letzter gespeicherter Zustand wurde geladen.\n")
    else:
        print("Keine gespeicherte Datei gefunden (Standardwerte verwenden).\n")
    
    while True:
        print("=== Kaffeeautomat ===")
        print("Unsere Getränke: Espresso | Latte | Cappuccino\n")
        
        choice = input("Getränk auswählen: ").lower().strip()
        if choice == "off":
            print("Automat wird ausgeschaltet")
            save_resources(resources)
            print("Zustand wurde in 'state.csv' gespeichert.")
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
        # Nach erfolgreicher Bestellung Resourcen in CSV speichern:
        save_resources(resources)
        print("Zutaten wurden aktualisiert. Zurück zur Startsituation...\n")

if __name__ == "__main__":
    main()