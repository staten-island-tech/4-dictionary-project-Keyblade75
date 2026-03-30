best_buy_items= item={     
    "name": "Samsung 55\" 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."}, 
item={"name": "Insignia 8' 4K Ultra HD HDMI Cable",
          "price": 30.00,
          "department":"Televisions",
          "description":"8' 4K HDMI cable for high quality video output."},
for index, item in enumerate(best_buy_items):
    print(index, ":", item["name"]) 
    print("Items in cart:", item["name"])     