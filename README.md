# Anforderungen

## Benutzerinteraktionen
- Espresso, Latte, Cappuccino
- Falsche oder ungültige Eingaben abgreifen

## Ausschalten des Automats
- Zum Ausschalten ein Geheimwort `off`
- Wartungspersonal hat extra Befehle mit Passwort

## Statusbericht
- Mit `report` geben wir einen Statusbericht aus
- Zeigt Ressourcen:
  ```
    Water: 150ml
    Milk: 50ml
    Coffee: 75g
    Money: 35,50€
  ```

## Zustandsprüfung
- Sind Zutaten vorhanden?
- Benutzerfreundliche MEldung ausgeben, falls Zutaten nicht vorhanden

## Bezahlvorgang
- Vorher Zutaten prüfen
- Nur Münzen erlaubt: `0,05€ | 0,10€ | 0,20€...`
- Annahme: Der Automat hat unendlich viel Rückgeld
- Prüfen ob echtes Geld
- Benutzer kann jederzeit Bezahlvorgang abbrechen

## Getränkezubereitung
- Erst nach erfolgreicher Zahlung
- Zutaten werden aufgebraucht

## Verbrauch der Zutaten
- Espresso:
  - 15 g Kaffee
  - 50 ml Wasser
  - 100 ml Milch

## Geheime Wartungsbefehle
- `Fill milk`: Milchvorrat zurücksetzen
- `Fill water`
- `Take money`

## Flowchart für Anwendung
<img src="img/Kaffeautomat_flowchart.png" alt="Flowchart Kaffeautomat" width=60%>

## Allgemeines zu CPS

<img src="CPS.png" alt="Flowchart Kaffeautomat" width=60%>


