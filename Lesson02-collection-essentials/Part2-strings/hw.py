#1
#john.smith, gmail.com

#2
# tqbf

#3
def extract_domain(email):
    number_of_at = email.count('@')
    if not number_of_at == 1:
        return 'invalid email'
    return email.slice[email.find('@'):]

#4
# 123456

#5
#MY_DOCUMENT

#6
# cherry

#7
def filter_numbers(text):
    new_text = ''
    for char in text:
        if not char in '1234567890':
            new_text += char 
    return new_text

#8
# https://example.com/users/profile 

#9
def count_character_types(text):
    character_types = {
        'letters':0,
        'digits':0,
        'spaces':0
        }
    for char in text:
        if 'a'<=char<='z' or 'A'<=char<='Z':
            character_types['letters'] += 1
        if char == ' ':
            character_types['spaces'] += 1
        if '0'<=char<='9':
            character_types['letters'] += 1
    return character_types
        
    