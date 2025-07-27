from pathlib import Path
import json

username = input("write your name:")

path = Path("username.json")
contents = json.dumps(username)
path.write_text(contents)

print(f"戻ってきた時も名前を憶えていますよ！ {username} さん！")