"""
Projekt: Kosten Manager
Ziel:
Ein einfaches Programm, mit dem Benutzer Einnahmen und Ausgaben speichern,
anzeigen und auswerten können.

Mögliche Funktionen:
- Ausgabe hinzufügen
- Einnahme hinzufügen
- Alle Einträge anzeigen
- Gesamtausgaben berechnen
- Gesamteinnahmen berechnen
- Aktuellen Kontostand berechnen
- Nach Kategorie filtern
"""


class Transaction:
    """
    Repräsentiert eine einzelne Buchung.

    Attribute:
    - amount: Betrag der Buchung
    - category: Kategorie, z. B. Essen, Miete, Freizeit
    - description: kurze Beschreibung
    - transaction_type: 'income' oder 'expense'
    - date: Datum der Buchung
    """

    def __init__(self, amount, category, description, transaction_type, date):
        # Hier Attribute speichern
        pass

    def display(self):
        # Gibt eine Buchung lesbar aus
        pass


class CostManager:
    """
    Hauptklasse für den Kosten Manager.

    Aufgaben:
    - Buchungen speichern
    - Neue Buchungen hinzufügen
    - Berechnungen durchführen
    - Daten anzeigen
    """

    def __init__(self):
        # Hier eine Liste für alle Buchungen erstellen
        pass

    def add_income(self, amount, category, description, date):
        # Neue Einnahme erstellen und speichern
        pass

    def add_expense(self, amount, category, description, date):
        # Neue Ausgabe erstellen und speichern
        pass

    def show_all_transactions(self):
        # Alle gespeicherten Buchungen anzeigen
        pass

    def calculate_total_income(self):
        # Alle Einnahmen zusammenrechnen
        pass

    def calculate_total_expenses(self):
        # Alle Ausgaben zusammenrechnen
        pass

    def calculate_balance(self):
        # Einnahmen minus Ausgaben berechnen
        pass

    def filter_by_category(self, category):
        # Nur Buchungen einer bestimmten Kategorie anzeigen
        pass


def show_menu():
    """
    Zeigt dem Benutzer ein Menü.

    Beispiel:
    1. Einnahme hinzufügen
    2. Ausgabe hinzufügen
    3. Alle Buchungen anzeigen
    4. Kontostand anzeigen
    5. Beenden
    """
    pass


def main():
    """
    Startpunkt des Programms.

    Hier soll:
    - ein CostManager-Objekt erstellt werden
    - eine Schleife laufen
    - der Benutzer eine Option auswählen
    - je nach Auswahl eine Methode aufgerufen werden
    """
    pass


if __name__ == "__main__":
    main()