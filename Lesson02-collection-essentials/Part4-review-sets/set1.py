#1
###2300

#2
###WOW WOW LFG

#3
def donations(dict):
    user_max = ''
    user_val = 0
    for key, value in dict.items():
        if value >= user_val:
            user_val = value
            user_max = key 
    return user_max
donation = {
    'neon': 250,
    'vibe' : 180,
    'lunar' : 400,
    'pixel' : 150
}
print(donations(donation))