best_buy_items=[{     
    "name": "Samsung 55 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
},
{
    "name":  "Insignia 8 4K Ultra HD HDMI Cable",
    "price": 30.00,
    "department":"Televisions",
    "description":"8' 4K HDMI cable for high quality video output."
},
{
    "name": "Play Station DualShock Wireless Contoller",
    "price": 60.00,
    "deprartment":"Gaming",
    "description":"insert description here"
},
{
    "name": "playstaion 5",
    "price":500.00,
    "department":"Gaming",
    "description":"insert description here"
}]

while user_input := "q":
    user_input = input("Enter the index of the item you want to know more about (or 'q' to quit)")
    for item in best_buy_items:
        if user_input == item["name"]:
            print(item["name"], "\n", item["price"], item["description"])