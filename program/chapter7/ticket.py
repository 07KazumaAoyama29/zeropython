flag = True
while flag:
    age = int(input("年齢を入力してください。終了の場合は-1を入力してください。"))
    if age < 0: flag = False
    elif age < 3: print("無料")
    elif age < 13: print("1,000yen")
    else: print("1,500yen")