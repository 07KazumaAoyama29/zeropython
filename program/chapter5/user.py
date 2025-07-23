users = ["admin", "kazuma", "hiroto", "haruto", "kanato"]
if not users: print("ユーザー募集中です！")
for name in users:
    if name == "admin": print("whats happen?")
    else: print(f"hello {name}")

current_users = users[:]
new_users = ["sota", "masayuki", "kei", "ton", "hiroto"]
for new in new_users:
    for now in current_users:
        if new.lower() == now.lower(): print(f"{new}、別の名前を入力してください。")
