pizzas = ["チーズ", "ハラペーニョ", "はらみ"]
for pizza in pizzas:
    print(f"ピザは{pizza}しか勝たん")
print("まぁ、あんまりピザは好きじゃないけどね。")

friend_pizzas = pizzas[:]
friend_pizzas.append("hello")
print(pizzas)
print(friend_pizzas)