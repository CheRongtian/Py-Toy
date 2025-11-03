user_0={
    'full name' : 'adam smith',
    'first name': 'adam',
    'last name' : 'smith'
}

for key, value in user_0.items():
    print(f"{key}")
    print(f"{value}\n")

alien_0 = {'colour' : 'green', 'points' : 5}
alien_1 = {'colour' : 'yellow', 'points' : 10}
alien_2 = {'colour' : 'red', 'points' : 15}

aliens=[alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)