#3
def create_username(first_name, last_name):
    username = first_name.lower() + '_' + last_name.lower()
    return username
print(create_username('John', 'Smith'))

#6
def check_email(email):
    valid = False 
    if '@' in email:
        if email.lower().endswith('.com'):
            valid = True 
    return valid
print(check_email('test@gmail.com'))
print(check_email('test@school.edu'))
#9
def create_slug(post):
    post = post.strip().lower().replace(' ','-')
    return post 
print(create_slug('   hi by the way by     '))