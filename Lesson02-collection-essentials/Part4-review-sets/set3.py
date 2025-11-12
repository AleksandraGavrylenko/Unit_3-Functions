#1
### [23]

#2
### NEXUS

#3
def match_mvp(players):
    max_k_to_d = 0
    max_person = ''
    for player, status in players.items():
        x = (status['kills'])/(status['deaths'])
        if x > max_k_to_d:
            max_k_to_d = x 
            max_person = player 
    return max_person
players = {
    'phoenix': {'kills':28, 'deaths':12},
    'cipher': {'kills':35, 'deaths':15},
    'blaze': {'kills':22, 'deaths':18}
}
print(match_mvp(players))