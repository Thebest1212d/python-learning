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

import sqlite3
import os

class SQLiteStorage: 
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "costmanager.db")
        self.conn = sqlite3.connect(db_path)

        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				amount REAL NOT NULL,
				category TEXT NOT NULL,
				description TEXT NOT NULL,
				transaction_type TEXT NOT NULL
					CHECK(transaction_type IN ('income', 'expense')),
				date TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def save_transaction(self, amount, category, description, transaction_type, date):
        sql = """
        INSERT INTO transactions 
        (amount, category, description, transaction_type, date)
        VALUES (?, ?, ?, ?, ?)
        """
        
        self.cursor.execute(sql, (amount, category, description, transaction_type, date))
        self.conn.commit()

    def get_all_transactions(self):
        self.cursor.execute("SELECT * FROM transactions")
        rows = self.cursor.fetchall()

        transactions = []

        for row in rows:
            transaction_id = row[0]
            amount = row[1]
            category = row[2]
            description = row[3]
            transaction_type = row[4]
            date = row[5]

            transaction = Transaction(transaction_id, amount, category, description, transaction_type, date)
            transactions.append(transaction)

        return transactions   
    
    def get_total_income(self):
        sql = "SELECT SUM(amount) FROM transactions WHERE transaction_type = ?"
        self.cursor.execute(sql, ("income",))
        result = self.cursor.fetchone()
        return result[0] if result[0] is not None else 0
    
    def get_total_expenses(self):
        sql = "SELECT SUM(amount) FROM transactions WHERE transaction_type = ?"
        self.cursor.execute(sql, ("expense",))
        result = self.cursor.fetchone()
        return result[0] if result[0] is not None else 0
    
    def delete_transaction(self, transaction_id):
        sql = "DELETE FROM transactions WHERE id = ?"
        self.cursor.execute(sql, (transaction_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def update_transaction(self, transaction_id, amount, category, description, transaction_type, date):
        sql = """UPDATE transactions
        SET amount = ?, category = ?, description = ?, transaction_type = ?, date = ?
        WHERE id = ?"""
        self.cursor.execute(sql, (amount, category, description, transaction_type, date, transaction_id))
        self.conn.commit()
        return self.cursor.rowcount

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

    def __init__(self, transaction_id, amount, category, description, transaction_type, date):
        # Hier Attribute speichern
        self.amount = amount
        self.category = category
        self.description = description
        self.transaction_type = transaction_type
        self.date = date
        self.transaction_id = transaction_id

    def display(self):
        # Gibt eine Buchung lesbar aus
        print(f"ID: {self.transaction_id} | {self.date} | {self.transaction_type.upper()} | {self.category} | {self.amount}€ | {self.description}")


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
        self.storage = SQLiteStorage()

    def add_income(self, amount, category, description, date):
        # Neue Einnahme erstellen und speichern
        self.storage.save_transaction(amount, category, description, "income", date)

    def add_expense(self, amount, category, description, date):
        # Neue Ausgabe erstellen und speichern
        self.storage.save_transaction(amount, category, description, "expense", date)

    def show_all_transactions(self):
        # Alle gespeicherten Buchungen anzeigen
        transactions = self.storage.get_all_transactions()
        for t in transactions:
            t.display()

    def calculate_total_income(self):
        return self.storage.get_total_income()

    def calculate_total_expenses(self):
        return self.storage.get_total_expenses()

    def delete_transaction(self, transaction_id):
        return self.storage.delete_transaction(transaction_id)
    
    def update_transaction(self, transaction_id, amount, category, description, transaction_type, date):
        return self.storage.update_transaction(transaction_id, amount, category, description, transaction_type, date)

    def calculate_balance(self):
        # Einnahmen minus Ausgaben berechnen
        balance = 0
        transactions = self.storage.get_all_transactions()
        for t in transactions:
            if t.transaction_type == "income":
                balance += t.amount
            else:
                balance -= t.amount
        return balance

    def filter_by_category(self, category):
        # Nur Buchungen einer bestimmten Kategorie anzeigen
        found = False
        transactions = self.storage.get_all_transactions()
        for i in transactions:
            if i.category.lower() == category.lower():
                i.display()
                found = True
            
        if (found == False):
            print("No info found")


def show_menu():
    #Zeigt dem Benutzer ein Menü.

        print("""
    ==== COST MANAGER ====
    1. Einnahme hinzufügen
    2. Ausgabe hinzufügen
    3. Alle Buchungen anzeigen
    4. Kontostand anzeigen
    5. Nach Kategorie filtern
    6. Transaktion löschen
    7. Transaktion bearbeiten
    8. Beenden
    """)

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

    while True:
        show_menu()
        cont = input("Wählen Sie bitte eine Ziffer: ")

        if (cont == "1"):
            try:
                amount = float(input("Betrag: "))
                category = input("Kategorie: ")
                description = input("Beschreibung: ")
                date = input("Datum: ")
                manager.add_income(amount, category, description, date)
                print("Income added!")
            except ValueError:
                print("Ungültiger Betrag")

        elif (cont == "2"):
            amount = float(input("Betrag: "))
            category = input("Kategorie: ")
            description = input("Beschreibung: ")
            date = input("Datum: ")
            manager.add_expense(amount, category, description, date)
            print("Expense added!")
        
        elif (cont == "3"):
            manager.show_all_transactions()      

        elif (cont == "4"):
            print("Current balance:", manager.calculate_balance())

            total_income = manager.calculate_total_income()
            print("Total income:", total_income)

            total_expense = manager.calculate_total_expenses()
            print("Total expense:", total_expense)

            #manager.filter_by_category("food")
            
        elif (cont == "5"):
            category = input("Kategorie eingeben: ")
            manager.filter_by_category(category)

        elif (cont == "6"):
            transaction_id = int(input("ID: "))
            deleted = manager.delete_transaction(transaction_id)

            if deleted:
                print("Deleted successfully")
            else:
                print("Transaction not found")

        elif (cont == "7"):
            transaction_id = int(input("ID: "))
            amount = float(input("Neuer Betrag: "))
            category = input("Neue Kategorie: ")
            description = input("Neue Beschreibung: ")
            transaction_type = input("income/expense: ")
            date = input("Neues Datum: ")

            updated = manager.update_transaction(
                transaction_id,
                amount,
                category,
                description,
                transaction_type,
                date
            )

            if updated:
                print("Transaction updated")
            else:
                print("Transaction not found")

        elif (cont == "8"):
            break

if __name__ == "__main__":
    main()