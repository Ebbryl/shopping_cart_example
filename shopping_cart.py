"""
E-commerce Shopping Cart System

This repository contains a simple e-commerce system that manages product listings
and shopping cart functionality. The system handles:

- Product listings with location-based shipping costs
- Shopping cart management (add/remove items)
- Stock tracking and updates
- Total price calculation including shipping

The system distinguishes between Java and non-Java locations for different
shipping costs (Rp. 2000 for Java, Rp. 5000 for other locations).
"""

class Listing:

    def __init__(self, name, location, price, stock):
        self.name = name
        self.location = location
        self.price = price
        self.stock = stock

    def shipping_cost(self):
        if self.location == 'jawa':
            return 2000
        else:
            return 5000

    def headline(self):
        return f'{self.name} dari warehouse pulau {self.location}' \
            f'(ongkir: Rp.{self.shipping_cost()} dengan harga Rp.{self.price}' \
            f'(stok tersedia {self.stock})'

    def update_stock(self, new_value):
        self.stock = new_value
    
class Shoppingcart:

    items_jawa = []
    items_non_jawa = []
    price = 0

    def __init__(self):
        return

    def add_items(self, item):
        if item.location == 'jawa':
            self.items_jawa.append(item)
        else:
            self.items_non_jawa.append(item)
        self.price += item.price
        item.stock -= 1

    def remove_items(self, item):
        if(item in self.items_jawa):
            self.items_jawa.remove(item)
            self.price -= item.price
            item.stock += 1
        if (item in self.items_non_jawa):
            self.items_non_jawa.remove(item)
            self.price -= item.price
            item.stock += 1

    def get_total_price(self):
        total_price = self.price
        if self.items_jawa:
            total_price += 2000
        if self.items_non_jawa:
            total_price += 5000

        return total_price

def main():
    """Main function to demonstrate the shopping cart functionality."""
    # Create product listings
    mixer   = Listing('mixer', 'jawa', 50000, 20)
    blender = Listing('blender', 'kalimantan', 30000, 20)
    tas     = Listing('tas murah kw1', 'kalimantan', 15000, 2)

    # Create shopping cart
    s = Shoppingcart()

    # Demonstrate adding items and stock tracking
    print(f"stock mixer: {mixer.stock}")

    # Add mixer to shopping cart
    s.add_items(mixer)

    # Current stock
    print(f"stock mixer: {mixer.stock}")

    # Total price need to pay
    print(f"total price: {s.price}")

    # Remove mixer from shopping cart
    s.remove_items(mixer)

    # Current stock
    print(f"stock mixer: {mixer.stock}")

    # Total price need to pay
    print(f"total price: {s.price}")

if __name__ == "__main__":
    main()
