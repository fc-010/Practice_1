import csv


class Inventory:
    def __init__(self):
        self.items = {}   # name -> (qty, price)

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def remove_item(self, name):
        if name not in self.items:
            
            raise KeyError(f"No item named {name}")
        del self.items[name]

    def total_value(self):
        total = 0
        for qty, price in self.items.values():
            total += qty * price
        return total

    def __len__(self):
        return len(self.items)


inv = Inventory()

with open("stock.txt") as f:
    for name, qty, price in csv.reader(f):
        try:
            inv.add_item(name, int(qty), int(price))
        except ValueError:
            print(f"Skipping {name}: bad number")

print(f"{len(inv)} items, total value {inv.total_value()}")

inv.remove_item("pen")
print(f"{len(inv)} items, total value {inv.total_value()}")

try:
    inv.remove_item("laptop")
except KeyError as e:
    print(f"Error: {e}")
