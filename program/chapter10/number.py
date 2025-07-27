from pathlib import Path
import json

path = Path("number.json")
if path.exists():
    contents = path.read_text()
    num = json.loads(contents)

    print(f"あなたの好きな数字は {num} です。")
else:
    num = input("あなたの好きな数字を入力してください:")
    contents = json.dumps(num)
    path.write_text(contents)