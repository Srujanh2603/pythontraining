#write a python program representing shopping cart include methods for adding and removing items and calculating the total price

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item,price,quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}
        print(f'Added {quantity} of {item} to cart')
    
    def remove_item(self, item,quantity=1):
        if item in self.items:
            if self.items[item]['quantity']<=quantity:
                del self.items[item]
                print(f'Removed all{item} from cart')
            else:
                self.items[item]['quantity']-=quantity
                print(f'Removed {quantity} of {item} from cart')
                
    def total_price(self):
        total = 0
        for item in self.items.values():
            total += item['price']*item['quantity']
        return total
        
    def displaycart(self):
        if not self.items:
            print('Cart is empty')
        else:
            print('Shopping cart: ')
            for item, details in self.items.items():
                print(f'{item}: {details['price']} x {details['quantity']}')
            print(f'Total: {self.total_price()}')


cart = ShoppingCart()
cart.add_item('apple', 10, 2)
cart.add_item('orange', 5)
cart.add_item('mango', 15)
cart.displaycart()
cart.remove_item('apple', 1)
cart.remove_item('mango', 2)
cart.displaycart()