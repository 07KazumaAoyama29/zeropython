guests = ["hiroto", "haruto", "sota"]
print(len(guests))
for i in guests:
    print(f"親愛なる{i}様、是非、夕食をご一緒させてください。")
absentees = "sota"
print(f"{absentees}は残念ながら欠席するみたいです。")
guests.remove(absentees)
guests.append("masayuki")
for i in guests:
    print(f"親愛なる{i}様、是非、夕食をご一緒させてください。")
print("さらに大きい席を見つけたので、追加で三人招待することになりました。")
guests.insert(0, "yuto")
guests.insert(int(len(guests) / 2), "seinosuke")
guests.insert(len(guests), "kanato")
for i in guests:
    print(f"親愛なる{i}様、是非、夕食をご一緒させてください。")

print("現在のテーブルでは夕食の時間に間に合わないため、二人しか招待できないことになりました。")
while len(guests) > 2:
    guets = guests.pop()
    print(f"{guets}、ごめん。今回はなしで。")
print(f"おめでとう。{guests[0]}は夕食に招待されたままです！")
del guests[0]
print(f"おめでとう。{guests[0]}は夕食に招待されたままです！")
del guests[0]
print(guests)