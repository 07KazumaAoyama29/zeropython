name = "Kazuma"
print(f"こんにちは{name}、今日は Python を学びますか？")

print(f"こんにちは{name.lower()}、今日は Python を学びますか？")
print(f"こんにちは{name.upper()}、今日は Python を学びますか？")
print(f"こんにちは{name.title()}、今日は Python を学びますか？")

print('ケネディは "若者は快楽よりも冒険に身をゆだねる" と言った。')
famous_person = "ケネディ"
message = f'{famous_person}は "若者は快楽よりも冒険に身をゆだねる" と言った。'
print(message)

name = "  \tkazuma\t\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

filename = "hun.txt"
print(filename.removesuffix(".txt"))