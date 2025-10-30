def format_phone_number(phone):
    cleaned = ''
    for i in phone:
        if i.isdigit():
            cleaned += i 
    if not len(cleaned) == 10:
        return 'invalid'
    return f'({cleaned[0:3]}) {cleaned[3:6]}-{cleaned[6:10]}'
print(format_phone_number('555-123-4567'))