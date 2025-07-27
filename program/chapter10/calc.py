num1 = input("一つ目の数字を入力してください:")
num2 = input("二つ目の数字を入力してください:")
while True:
    try:
        ans = int(num1) + int(num2)
    except ValueError:
        print(f"数値を入力してください。")
        num1 = input("一つ目の数字を入力してください:")
        num2 = input("二つ目の数字を入力してください:")
    else:
        # ファイル内のだいたいの単語の数を数える
        print(ans)
        break