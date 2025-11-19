def search_data(query):
    if query == '':  #no query provided
        return None
    if query == 'empty':  #found zero results
        return 0
    if query == 'error':   # search failed
        return False
    return len(query)  # normal case - return count

#1  return type - None --> 'no value'
#meaning : absense of value, not set, not found
#use for: missing data, search failures, optional parameters
result = None
print(result is None) # True --> identity check
print(result == None) # True --> equality check
print(not result)  #True --> falsy check

#2   return type - False --> not true
#meaning - explicid false condition, validation failure, negative result
# use for: validation result, boolean operations, success/failure status
result = False 
print(result is False) #True - identity check
print(not result) #True - boolean negation
print(result == 0)  #True - falsy check


#3  return type - 0 --> A valid number
# zero is VALID numeric value, not absence of value
result = 0
print(result == 0) #True  - numerical value
print(not result)  # True - falsy in boolean context
print(result is None) #False - since it's a different object
print(result is False) #False - defferent types


#multiple returns - python packs multiple returns into a tuple
def claculate_room(length, width):
    area = length*width 
    perimeter = 2*(length+width)
    return area, perimeter  #turns into a tuple (area, perimeter)
result = claculate_room(10,5)
print(result)
print(type(result))

no_parenthesis = 1,2,3 #still a tuple

#unpacking tuple
area, perimeter = claculate_room(10,5)
print('area:' , area)
print('perimeter:' , perimeter)


