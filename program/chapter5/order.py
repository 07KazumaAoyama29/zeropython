order = list(range(1, 10))
for num in order:
    if num == 1: print("1st")
    elif num == 2: print("2nd")
    elif num == 3: print("3rd")
    elif num > 3: print(f"{num}th")
    else: print("invalid number!")