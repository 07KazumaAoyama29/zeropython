names = ["abel", "tim", "carl", "jun", "peter"]
print("リストの最初の3つの要素です")
for name in names[:3]:
    print(name)
print("リストの中央の3つの要素です")
center = int(len(names) / 2) 
for name in names[center -1 : center + 2]:
    print(name)
