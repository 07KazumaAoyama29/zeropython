from pathlib import Path

name = ""
while True:
    tmp = input("名前を入力して下さい:")
    if tmp == "q": break
    name += f"{tmp}\n"

path = Path("guests.txt")
path.write_text(name)