#3
def getPhoneNumber(contacts,name):
    try:
        return contacts[name]
    except KeyError:
        return 'contact not found'
    
phone_nums = {'Mom':'555-0123','Dad':'555-0124','Best Friend':'555-0125'}
print(getPhoneNumber(phone_nums,'Mom'))
print(getPhoneNumber(phone_nums,'Boss'))
'''works!'''

#4
def getSong(playlist,index):
    try:
        return playlist[index]
    except IndexError:
        return 'position out of range'
    except TypeError:
        return 'position must be an integer'
songs = ['a','b','c','d','e']
print(getSong(songs,2))
print(getSong(songs,45))
print(getSong(songs,'one'))
'''works!'''

#5
def calculate_test_avg(*scores):
    try:
        return (sum(scores))/(len(scores))
    except ZeroDivisionError:
        return 0
    except TypeError:
        return 'invalid score data'
    except Exception as e:
        return f'unfortunately, an error occured. Error: {e}'
print(calculate_test_avg(45,56,67,78,89,90))
print(calculate_test_avg(45.5,56.7,67.8,78.9,89.0,90.0))
print(calculate_test_avg(45.5,56.7,67.8,78.9,89.0,'90.0'))
print(calculate_test_avg())
'''works'''