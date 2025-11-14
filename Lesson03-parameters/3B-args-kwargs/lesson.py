#1
def calculate_cart_total(*prices):
    """calculating total for any number of items
    prices (float) - variable number of prices
    returns total of all prices rounded to two decimals
    """
    #check if cart is empty
    if not prices:
      return 0.00
    #sum all prices
    subtotal = sum(prices)
    #round to two decimals and return
    return round(subtotal, 2)
print(f'empty cart: ${calculate_cart_total()}')
print(f'1 item: ${calculate_cart_total(19.99)}')
print(f'3 item: ${calculate_cart_total(19.99, 12.34, 67.67)}')
print(f'4 item: ${calculate_cart_total(19.99, 12.34, 67.67, 41.41)}')
# **kwargs
def create_order(customer_name, **items):
    """Create an order w any menu items"""
    order = {
        'customer name': customer_name,
        'items': items,
        'item count': len(items),
    }
    return order 
order1 = create_order('Samuel', pizza=2,wings=4, soda = 4, ice_cream = 7)
order2 = create_order('Chadifer', burger = 4, taco = 7, fries = 3)
order3 = create_order('Barb', salad = 1, water = 1, fries = 1)
print(order1)
print(order2)
print(order3)

#order for parameters
def function(required,*args, default=10, **kwargs):
    print()