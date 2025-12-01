#The raise syntax
#basic syntax
'''
raise ExceptionType('ur message')
Ex:
raise ValueError('quantity must be at least 1)
raise TypeError('expected player object, got a potato')
raise PerimissionError('ur not a mod, nice try tho')
'''
#just returning
def open_loot_box1(player, qty):
    if qty<=0:
        return None 
    #rest of the code
#raising exception
def open_loot_box2(player, qty):
    if qty<=0:
        raise ValueError('bad quantity')
    #rest of the code
    
VALID_PROTEINS = ['chicken','steak','barbacoa','carnitas']
VALID_RICE = ['white','brown','none']
VALID_BEANS = ['black','pinto','none']
MAX_FREE_EXTRAS = 3

def build_bowl(protein, rice, extras):
    """Build a chipotle bowl with validation

    Raises:
    ValueError -> if protein is invalid
    TypeError -> if extras is not a list
    """
    #check if extras is a list
    if not isinstance(extras,list):
        raise TypeError('extras must be a list')
    #validate protein
    if protein.lower()not in VALID_PROTEINS:
        raise ValueError(f'"{protein}" isnt valid! Choose from {VALID_PROTEINS}')
    #return the bowl
    return {
        'protein': protein.lower(),
        'rice' : rice,
        'extras':extras,
        'price': 10.50
    }
    
try:
    bowl = build_bowl('chicken','brown','corn')
    print(f'created {bowl}')
except Exception as e:
    print(f'Error: {e}')