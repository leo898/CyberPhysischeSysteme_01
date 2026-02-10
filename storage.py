"""
Speichert und lädt den Automatenzustand (resources) in/aus einer CSV-Datei.
"""

import csv
from typing import Dict
import os

DEFAULT_STATE_FILE = "state.csv"

def save_resources(resources: Dict[str, float], filename: str = DEFAULT_STATE_FILE) -> None:
    """
    Speichert alle Ressourcen in eine CSV-Datei.
    Format:
    key, value
    water_ml, 150
    milk_ml: 150
    ...
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Die Kopfzeile:
        writer.writerow(["key", "value"])
        # Der eigentliche Inhalt:
        for key, value in resources.items():
            writer.writerow([key, value])

def load_resources(resources: Dict[str, float], filename: str = DEFAULT_STATE_FILE) -> bool:
    """
    Lädt Ressourcen aus CSV-Datei und überschreibt die Werte im Dictionary 'resources'.
    Rückgabe:
    - True, wenn erfolgreich geladen
    - False, wenn Datei nicht vorhanden (dann bleiben default-Werte)
    """
    if not os.path.exists(filename):
        return False

    with open(filename, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key=row["key"]
            value_str = row["value"]
            
            # Zahlen in Float konvertieren:
            try:
                value = float(value_str)
            except ValueError:
                continue
            
            # Nur bekannte keys überschreiben:
            if key in resources:
                resources[key] = value
    return True
    
    
    