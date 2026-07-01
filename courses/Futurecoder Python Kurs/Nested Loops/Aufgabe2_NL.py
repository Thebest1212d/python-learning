players = ["Alice", "Bob", "Charlie"]
for i in range(len(players)):
    for j in range(len(players)):
        if i != j:
            print(f"{players[i]} vs {players[j]}")