def city_country(city, country, population = ""):
    if population:
        return f"{city}, {country} - 人口{population}"
    else:
        return f"{city}, {country}"

if __name__ == "__main__":
    print(city_country("Akashi", "Japan"))
    print(city_country("Toronto", "Canada"))
    print(city_country("Tokyo", "Japan"))