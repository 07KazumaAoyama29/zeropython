message = "hello"
print(message)

message = "rewrite"
print(message)

#文字列メソッドで大文字小文字を変える
name = "kazuma aoyama"
print(name.title())

name = "AdA"
print(name.upper())
print(name.lower())

first_name = "Kazuma"
last_name = "Aoyama"
full_name = f"{first_name} {last_name}"
message = f"こんにちは{full_name}!"
print(message)

#タブを加える
print("\tPython")
#改行を加える
print("Languages:\nPython\nC\nJavaScript")

#空白文字の削除(左端・右端のみ)
favorite_language = " Python "
print(favorite_language)
rsted_faverite_language = favorite_language.rstrip()
print(rsted_faverite_language)
lsted_faverite_language = favorite_language.lstrip()
print(lsted_faverite_language)
sted_favorite_language = favorite_language.strip()
print(sted_favorite_language)

#接頭辞を削除
nomal_url = "https://rm.lsnl.jp/"
print(nomal_url.removeprefix("https://"))
print(nomal_url)#removeprefixを実行しても変数の中身は変更されない

print(1+7)
print(10-2)
print(2*4)
print(int(16/2))
favorite_num = 666
print(f"私の好きな数字は{favorite_num}です。")
