#q 5-8 from the practice

#5
'''
1) 20 - 20*0.1 = 18
2) 10 + 5 = 15
'''

#6
def make_notification(user, *messages, urgent=False):
    if not user:
        return 'no user = invalid notification'
    notif = ''
    if urgent:
        notif += 'URGENT: '
    notif += user + ' - '
    for m in messages:
        m = str(m)
        notif += m
        if not m == messages[-1]:
            notif += ', '
    return notif
        
print(make_notification("admin", "Server down!", urgent=True))  # Should return: "URGENT: admin - Server down!"
print(make_notification("user", "Welcome", "Check inbox"))  # Should return: "user - Welcome, Check inbox"

#7
'''
1) SELECT name, email FROM users
2) SELECT * FROM logs WHERE level = 'error' LIMIT 5
'''
#8
def log_action(actor, *actions, timestamp=None, **context):
    if not actor:
        return 'actor required'
    message = f'{actor}: '
    for a in actions:
        a = str(a)
    str_actions = ', '.join(actions)
    message += str_actions + ' | '
    for key, value in context.items():
        message += f'{key}={value} '
    return message 

print(log_action("bot", "login", "scan", source="API", ip="1.2.3.4"))  # Should return: "bot: login, scan | source=API, ip=1.2.3.4"
    
    
