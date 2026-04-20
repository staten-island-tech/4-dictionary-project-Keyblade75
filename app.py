best_buy_items= item=[{     
    "name": "Samsung 55\" 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."}, 
{"name":  "Insignia 8 4K Ultra HD HDMI Cable",
          "price": 30.00,
          "department":"Televisions",
          "description":"8' 4K HDMI cable for high quality video output."},
          {"name": "Play Station DualShock Wireless Contoller",
          "price":60.00,
          "deprartment":"gaming",
          "description":"insert description here"},
          {"name": "playstaion 5",
          "price":500.00,
          "department":"Gaming",
          "description":"insert description here"},]
for index, item in enumerate(best_buy_items):
 print(index,"Items in cart:", item["name"],item["price"])     