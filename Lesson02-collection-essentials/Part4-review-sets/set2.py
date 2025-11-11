#1
### 4
### 1300 + 1500 + 2700 + 1500 = 7000

#2
### '0x9F1aB3c....'

#3
def portfolio_value(holdings,price):
    total = 0.0
    for key in holdings.keys():
        total += (holdings[key]*price[key])
    return round(total, 2)
holdings = {'BTC': 0.5, 'ETH': 8.2, 'SOL':50}
prices = {'BTC': 62400, 'ETH': 2480, 'SOL':142}
print(portfolio_value(holdings,prices))