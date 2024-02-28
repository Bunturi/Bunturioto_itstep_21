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
