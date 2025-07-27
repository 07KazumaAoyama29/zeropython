from restaurant import Restaurant, IceSreamStand

my_restaurant = Restaurant("hiroto", "焼肉")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

akashi_resutaurant = Restaurant("kagoya", "明石焼き")
kobe_restaurant = Restaurant("hikiniku", "洋食")

akashi_resutaurant.describe_restaurant()
kobe_restaurant.describe_restaurant()

ice_shop = IceSreamStand("31", "アイス", "抹茶")
ice_shop.describe_flavor()