from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()

birthday = input("誕生日をmmddyyフォーマットで入力してください:\n")
if birthday in pi_string:
    print("success")
else:
    print("fail")

print(pi_string[:52])
print(len(pi_string))