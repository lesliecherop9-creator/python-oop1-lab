class Coffee:
    def __init__(self, coffee_type, size, price):
        self.coffee_type = coffee_type
        self.size = size
        self.price = price

    def tip(self):
        print(f"You tipped your {self.size} {self.coffee_type}!")