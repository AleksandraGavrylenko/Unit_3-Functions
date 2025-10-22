def calc_discount(price, member_status):
    if member_status == 'premium':
        return price*0.7
    elif member_status == 'standard':
        return price*0.85
    else:
        return price
    
print(calc_discount(100,'premium'))
print(calc_discount(100,'standard'))
print(calc_discount(100,'guest'))

def count_vowel(word):
    count = 0
    vowels = 'AEIOUaeiou'
    for i in word:
        if i in vowels:
            count += 1
    return count 
print(count_vowel('Hello world'))

