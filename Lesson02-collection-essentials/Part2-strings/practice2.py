def format_phone_number(phone):
    cleaned = ''
    for i in phone:
        if i.isdigit():
            cleaned += i 
    if not len(cleaned) == 10:
        return 'invalid'
    return f'({cleaned[0:3]}) {cleaned[3:6]}-{cleaned[6:10]}'
print(format_phone_number('555-123-4567'))

def sanitize_filename(filename):
    cl_filename = filename.lower().replace(' ','_')
    for char in cl_filename:
        if not char.isdigit() and not char.isalpha():
            if not char in '._-':
                cl_filename.replace(char,'')
    if filename[-4] == '.':
        