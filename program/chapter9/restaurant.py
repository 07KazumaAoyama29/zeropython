class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.restaurant_type = type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"このレストランの名前は {self.restaurant_name} です。")
        print(f"このレストランは {self.restaurant_type} 専門店です。")
    
    def open_restaurant(self):
        print("開店します！！")
    
    def set_number_served(self, num):
        self.number_served = num
    
    def increment_number_served(self, num):
        self.number_served += num

class IceSreamStand(Restaurant):
    def __init__(self, name, type, flavors):
        super().__init__(name, type)
        self.flavors = flavors
    
    def describe_flavor(self):
        print(self.flavors)

