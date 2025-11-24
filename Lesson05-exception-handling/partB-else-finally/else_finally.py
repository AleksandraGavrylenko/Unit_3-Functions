'''if/else vs try/except'''
try:
    #try smth risky
    score = 4 #int(input('enetr score'))
except ValueError:
    #runs if failed
    print('invalid score')
else:
    #runs if succeeded
    print(f'score recorded: {score}')
    
def parse_command(message):
    '''parse a discord like: !ban PlayerName 7days'''
    try:
        parts=message.split()
        command = parts[0]
        target = parts[1]
        duration = parts[2]
    except IndexError:
        print('❌invalid command format, missng parts')
        return None 
    else:
        print(f'✅ command parsed succefully')
        if command.startswith('!'):
            print(f'⚡excecuting {command}')
        return command, target, duration
    finally:
        print('this block runs regardless!')
result = parse_command('!ban PlayerName 7day')
print(result)
result = parse_command('!ban PlayerName')
print(result)