cities = {
    "Akashi": {"country": "Japan", "population": 300_000, "fact": "good"},
    "Kobe": {"country": "Japan", "population": 1_500_000, "fact": "bad"},
    "Tokyo": {"country": "Japan", "population": 14_000_000, "fact": "very good"}
}
for name in cities.keys():
    print(f"{name}は{cities[name]["country"]}にあって、人口は{cities[name]["population"]}で、都市の状態は{cities[name]["fact"]}です。")