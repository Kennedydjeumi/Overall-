import random 
players = {"John Doe":random.randint(60,99), "Jane Smith": random.randint(80,99), "Bob Johnson":random.randint(90,100), "Alice Brown": random.randint(96,99),}

halved_overalls = {name: overall / 2 for name, overall in players.items()}

sorted_halved_overalls = sorted(halved_overalls.items(), key=lambda x: x[1], reverse=True)

print("Top 3 Defenders:\n")
for name, overall in sorted_halved_overalls[:3]:
    print(f"{name}: {overall}")

players = {"Joe scewer":random.randint(90,99), "simon your": random.randint(80,99), "bane robert":random.randint(70,100), "born alas":random.randint (70,99),}

halved_overalls = {name: overall / 2 for name, overall in players.items()}

sorted_halved_overalls = sorted(halved_overalls.items(), key=lambda x: x[1], reverse=True)

print("Top 1 Attackers :\n")
for name, overall in sorted_halved_overalls[:1]:
    print(f"{name}: {overall}")


players = {"robinik kilo":random.randint(60,99), "dean j labyrith ": random.randint(80,99), "scoupe noer":random.randint(90,100), "nice okio": random.randint(96,99),}

halved_overalls = {name: overall / 2 for name, overall in players.items()}

sorted_halved_overalls = sorted(halved_overalls.items(), key=lambda x: x[1], reverse=True)

print("Top 3 midfielders  :\n")
for name, overall in sorted_halved_overalls[:3]:
    print(f"{name}: {overall}")