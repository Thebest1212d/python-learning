# =========================
# INVENTORY REPORT
# =========================

# Gesamtanzahl Geräte: 10

# Geräte pro Kategorie
# --------------------
# Notebook: 4
# Monitor: 2
# Desktop: 1
# Tablet: 1
# ...

# Geräte pro Hersteller
# ---------------------
# Lenovo: 5
# Dell: 3
# HP: 2

# Ältestes Kaufdatum:
# 2022-03-15

# Neueste Garantie:
# 2030-01-12

import pandas as pd

df = pd.read_csv("data/sample_inventory.csv")

device = len(df)
category_counts = df["Kategorie IT"].value_counts()

manufacturer_counts = df["Modell"].str.split(" ").str[0].value_counts()

old_date = df["Kaufdatum"].min()
new_garant = df["Garantie"].max()

print(" =========================")
print(" INVENTORY REPORT")
print(" =========================")
print("Gesamtanzahl Geräte:", device)
print("\nGeräte pro Kategorie:")
print(category_counts)
print("\nGeräte pro Hersteller")
print(manufacturer_counts)
print("Ältestes Kaufdatum:\n", old_date)
print("Neueste Garantie:\n", new_garant)