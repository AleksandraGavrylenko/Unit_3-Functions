#1
###{'key_a':'value1', 'key_b':150, 'key_d':50}:
###False

#2
###120
###60

#3
def get_user_bio(user):
    if not user.get('bio',0) == 0:
        return user['bio']
    return 'no bio available'
    #better to just do #return user.get('bio','no bio available')
print(get_user_bio({"username": "coder","bio": "Python enthusiast"})) # "Python enthusiast"

print(get_user_bio({"username": "newbie"})) # "No bio available"

#4
###60
###160

#5
###2

#6
def get_total_engagement(post):
    return post.get('likes',0) + post.get('comments',0) + post.get('shares',0)

print(get_total_engagement({"likes": 100,"comments": 20,"shares": 10})) # 130
print(get_total_engagement({"likes": 50,"comments": 5})) # 55
print(get_total_engagement({"views": 1000})) # 0

#7
###3
###3

#8
###{'key_1':'value_1','key_2':200,'key_3':50}
###{'key_1':'value_1','key_2':100,'key_4':True}

#9
def find_most_followed(users):
    if users:
        most_followed = ''
        most_followers = 0
        for user in users:
            if user['followers'] > most_followers:
                most_followers = user['followers']
                most_followed = user['username']
        return most_followed
    return None
users = [

{"username": "alex"
,
"followers": 1000},

{"username": "sam"
,
"followers": 5000},

{"username": "jordan"
,
"followers": 3000},

# {'username':'michael',
#  'followers':100000},
]
print(find_most_followed(users))