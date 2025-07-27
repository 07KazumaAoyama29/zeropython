from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text(encoding='utf-8')
contents = contents.replace("Python", "C言語")
print(contents)

lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))