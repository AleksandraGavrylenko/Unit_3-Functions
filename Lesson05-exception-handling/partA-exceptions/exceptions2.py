def saf_divide(a,b):
    try:
        result = a/b
        return result 
    # except:
    #     print('cannot divide by zero')
    #     return None 
    except ZeroDivisionError:
        print('cannot divide by zero')
        return None 
    except TypeError:
        print('not a valid number')
        return None
    except:
        print('an error occured...')
print(saf_divide(10,0))

def safe_operations(a,b,lst,key,d):
    try:
        print(f'division result: {a/b}') #zero division error, type error
        print(f'access list element:',lst[2]) #indexError
        print(f'access dictionary element:',d[key]) #keyError
        print(f'add numbers: {a+b}') #type error
    except ZeroDivisionError:
        print('cannot divide by 0')
    except IndexError:
        print('list index out of range')
    except KeyError:
        print(f'key {key} not found in dictionary')
    except TypeError:
        print('invalid types of operation')
    except Exception as e:
        print('some other error occured',e)
        
print(safe_operations(10,2,[1,2],'Tom',{'John':15}))
print(safe_operations(10,0,[1,2],'Tom',{'John':15}))

def calculate_price_per_item(tCost,nItems):
    try:
        pPerItem = tCost/nItems
        return pPerItem
    except ZeroDivisionError:
        print('cannot divide by zero')
        return None 
    except TypeError:
        print('invalid input, only int allowed')
        return None 
    except Exception as e:
        print('an error occured: ',e)
        return None 
print(calculate_price_per_item(100,2))

def parse_age(ageStr):
    try:
        return int(ageStr)
    except TypeError:
        print('a type error occured')
        return None