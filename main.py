from config import MENU, resources, MAINTENANCE_CODE
from utils import euro_formater
from payment import payment_process
from machine import (
    report, ingredients_ok, handle_change_and_profit,
    make_drink, deduct_ingredients, fill_water,
    fill_milk, fill_coffee, take_money 
    )
from storage import save_resources, load_resources

def maintenance_mode(required_code: bool = True) -> None:
    """
    Wartungsmodus (Service-Menü)
    """
    print("\n--- WARTUNGSMODUS ---")
    
    if required_code:
        code = input("Codewort eingeben: ").strip()
        if code != MAINTENANCE_CODE:
            print("Falsches Codewort. Wartungsmodus abgebrochen.\n")
            return
        print("Wartungsmodus aktiviert")
        print("Befehle: fill water | fill milk | fill coffee | take money | report | exit\n")
        
        while True:
            cmd = input("wartungs> ").strip().lower()
            if cmd == "exit":
                print("Wartungsmodus verlassen.\n")
                return
            
            elif cmd == "report":
                report()
                continue
            
            elif cmd == "fill water":
                fill_water()
                save_resources(resources)
                print("Wasser aufgefüllt und gespeichert.\n")

            elif cmd == "fill milk":
                fill_milk()
                save_resources(resources)
                print("Milch aufgefüllt und gespeichert.\n")
                
            elif cmd == "fill coffee":
                fill_coffee()
                save_resources(resources)
                print("Kaffee aufgefüllt und gespeichert.\n")
                
            elif cmd == "take money":
                taken = take_money()
                save_resources(resources)
                print(f"Geld entnommen: {euro_formater(taken)} (Zustand gespeichert)\n")
            
            else:
                print("Unbekannter Befehl, elaubt ist: fill water | fill milk | fill coffee | take money | report | exit\n")
            
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
            maintenance_mode(required_code=True)
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