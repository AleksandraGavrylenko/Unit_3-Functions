#2
def find_top_players(players, min_score):
    usernames = []
    for i in players:
        if i['score'] >= min_score:
            usernames += i['username']
    return usernames

#3
###9
### EYE OF THE TIGER
### BLINDING LIGHTS

#4
def calculate_cart_total(cart):
    total_price = 0
    for item in cart:
        total_price += item['price']
    return total_price
        