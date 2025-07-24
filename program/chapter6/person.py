people_1 = {"last_name":"Ono", "first_name": "hiroto", "age": 12, "city": "Kobe"}
people_2 = {"last_name":"Mitani", "first_name": "haruto", "age": 13, "city": "Kobe"}
people_3 = {"last_name":"Niwa", "first_name": "kanato", "age": 10, "city": "Kobe"}
people = [people_1, people_2, people_3]
for dic in people:
    for key in dic.keys():
        print(f"{key}: {dic[key]}")
favorite_num = {
    "kazuma": [666, 66],
    "hiroto": [7, 777],
    "haruto": [100, 55],
    "masayuki": [0, -2],
    "kanato": [1, 11]
}
for name in favorite_num.keys():
    print(f"{name}: {favorite_num[name]}")