# SCOPE - The visibility of variables, where it can be seen and used
# GLOBAL -outside all functions, so any function can use them
# LOCAL - inside a function, and only visible there

#The BUG
def add_bonus():
    score = score + 100 #python thinks its local # crashes
score = 500
add_bonus()