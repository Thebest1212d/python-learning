players = ['Charlie', 'Alice', 'Dylan', 'Bob']
for i in range(len(players)):
    for j in range(i + 1, len(players)):
        if i != j:
            print(f"{players[i]} vs {players[j]}")


# Beispiel von Kurs
# players = ['Charlie', 'Alice', 'Dylan', 'Bob']
# for i in range(len(players)):
#     for j in range(len(players)):
#         if i < j:
#             print(f'{players[i]} vs {players[j]}')