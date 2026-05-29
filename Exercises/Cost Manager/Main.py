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
        self.amount = amount
        self.category = category
        self.description = description
        self.transaction_type = transaction_type
        self.date = date
        pass

    def display(self):
        # Gibt eine Buchung lesbar aus
        print(f"{self.date} | {self.transaction_type.upper()} | {self.category} | {self.amount}€ | {self.description}")
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
        self.transactions = []
        pass

    def add_income(self, amount, category, description, date):
        # Neue Einnahme erstellen und speichern
        transaction = Transaction(amount, category, description, "income", date)
        self.transactions.append(transaction)
        pass

    def add_expense(self, amount, category, description, date):
        # Neue Ausgabe erstellen und speichern
        transaction = Transaction(amount, category, description, "expense", date)
        self.transactions.append(transaction)
        pass

    def show_all_transactions(self):
        # Alle gespeicherten Buchungen anzeigen
        for i in self.transactions:
            i.display()
        pass

    def calculate_total_income(self):
        # Alle Einnahmen zusammenrechnen
        pass

    def calculate_total_expenses(self):
        # Alle Ausgaben zusammenrechnen
        pass

    def calculate_balance(self):
        # Einnahmen minus Ausgaben berechnen
        balance = 0
        for t in self.transactions:
            if t.transaction_type == "income":
                balance += t.amount
            else:
                balance -= t.amount
        return balance

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
    manager = CostManager()

    manager.add_income(1000, "Salary", "Monthly salary", "2025-06-01")
    manager.add_expense(200, "Food", "Groceries", "2025-06-02")

    print("Current balance:", manager.calculate_balance())

    manager.show_all_transactions()

    pass


if __name__ == "__main__":
    main()