from city import city_country

def test_city_country():
    """'Janis Joplin' のような名前で動作するか？"""
    name = city_country("Akashi", "Japan")
    assert name == 'Akashi, Japan'
    name = city_country("Toronto", "Canada")
    assert name == 'Toronto, Canada'
    name = city_country("Tokyo", "Japan")
    assert name == 'Tokyo, Japan'
    