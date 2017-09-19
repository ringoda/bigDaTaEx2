# Dictionaries for inventory of a store
Price = {
    'Couch': 599,
    'TV': 710,
    'Coffee table': 70,
    'Bed': 349,
    'Table': 199
}

Inventory = {
    'Couch': 5,
    'TV': 10,
    'Coffee table': 19,
    'Bed': 7,
    'Table': 13
}

# Calculated the value of the inventory
value = 0
for key in Price:
    value += Price[key]*Inventory[key]
print value

# Calculated the value of the inventory if the price of coffee tables are decreased by 20% and TV by 10%
value_dec = 0
for key in Price:
    if key == 'Coffee table':
        value_dec += Price[key]*0.8*Inventory[key]
    elif key == 'TV':
        value_dec += Price[key]*0.9*Inventory[key]
    else:
        value_dec += Price[key]*Inventory[key]
print value_dec

# another way of solving the second task
Price['Coffee table'] = Price['Coffee table']*0.8
Price['TV'] = Price['TV']*0.9
value_dec2 = 0
for key in Price:
    value_dec2 += Price[key]*Inventory[key]
print value_dec2



