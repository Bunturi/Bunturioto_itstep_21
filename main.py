import json


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, quantity: {self.quantity}"


# Custom encoder function to handle serialization of Product objects
def custom_encoder(obj):
    if isinstance(obj, Product):
        return {
            "name": obj.name,
            "price": obj.price,
            "quantity": obj.quantity
        }
    return obj


# Custom decoder function to handle deserialization of Product objects
def custom_decoder(json_data):
    return Product(json_data['name'], json_data['price'], json_data['quantity'])


# Sample Product objects
products = [
    Product("Apple", 2.49, 5),
    Product("Mandarin", 1.49, 3),
    Product("Orange", 2.89, 4),
    Product("Banana", 5.99, 2),
    Product("Potatoes", 1.2, 10),
    Product("Onion", 1.5, 5),
    Product("Carrot", 1.1, 8),
    Product("Broccoli", 2.2, 1)
]


# Serialize the Product objects to a JSON file
with open("product.json", "w") as json_file:
    json.dump(products, json_file, default=custom_encoder, indent=4)


# Deserialize the JSON file back to Python objects
with open("product.json", "r") as read_json:
    python_data = json.load(read_json, object_hook=custom_decoder)

# Display the deserialized Python objects
for data in python_data:
    print("product:", data.name)
    print("price:", data.price)
    print("quantity:", data.quantity)
    print()
