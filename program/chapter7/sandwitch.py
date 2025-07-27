order_list = ["egg", "tuna", "egg", "egg"]
made_list = []
while order_list:
    made_list.append(order_list.pop())
print(made_list)

while "egg" in made_list:
    made_list.remove("egg")
print(made_list)