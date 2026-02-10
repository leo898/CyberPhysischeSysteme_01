"""
Enthlält alle festen Daten und Startwerte (Konfiguration + Systemzustand)
"""

# Das ist das Menu mit benötigten Ressourcen pro Getränk:
MENU = {
    "espresso": {
        "price": 8.80,
        "needs": {"water_ml": 50, "milk_ml": 100, "coffee_g": 15}
    },
    "cappuccino": {
        "price": 5.20,
        "needs": {"water_ml": 50, "milk_ml": 200, "coffee_g": 15} 
    },
    "latte": {
        "price": 4.80,
        "needs": {"water_ml": 0, "milk_ml": 250, "coffee_g": 25} 
    }
}

# Erlaubte Münzen:
ACCEPTED_COINS = [0.05, 0.10, 0.20, 1.00, 2.00]

# Systemzustand / Ressourcen:
resources = {
    "water_ml": 150,
    "milk_ml": 300,
    "coffee_g": 75,
    "money_eur": 35.50
}

MAX_RESOURCES = {
    "water_ml": 150,
    "milk_ml": 300,
    "coffee_g": 75,
}

# Optionales Codewort für den Wartungsmodus:
MAINTENANCE_CODE = "admin123"