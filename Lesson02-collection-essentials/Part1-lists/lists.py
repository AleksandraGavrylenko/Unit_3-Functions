'''
py
create: [1,2,3]
add: .append(val)
remove end: .pop()
insert: 
len
max
min
sum
'''

#creating lists
daily_likes = [500,600,750,400]
usernames = ['@nasa','@tswift','@netflix']
mixed_data = [500,'likes','@user123',True]
#accessing elements
first_day = daily_likes[0]
last_day = daily_likes[-1]
third_day = daily_likes[2]
#slicing
first_three = daily_likes[0:3]
last_two = daily_likes[-2:0]

#code along post analyzer
def analyze_post(likes_list):
    if likes_list:
        total = sum(likes_list)
        average = total / len(likes_list)
        best_day = max(likes_list)
        return (average, best_day)
    return 'the list is empty'
print(analyze_post(daily_likes))

#p 1
user_list = ['nasa','tswift','netflix']
def format_usernames(list):
    list_mod = []
    for i in user_list:
        list_mod.append('@'+i)
    return list_mod 
print(format_usernames(user_list))

#p 2
def filter_trending(list):
    list_mod = []
    for i in list:
        if i >= 1000:
            list_mod.append(i)
    return list_mod
print(filter_trending([500,1200,800,1500,600]))