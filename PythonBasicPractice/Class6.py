from random import randint

a = randint(1,6)
print (a)

from random import choice

players = ['mason', 'harry', 'bruno', 'fred', 'scott']
first_up = choice(players).title()
print(first_up)