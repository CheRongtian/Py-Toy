pizza ={
    'crust' : 'thick',
    'toppings' : ['mushrooms','extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")


favourite_laguage={
    'jen' : ['python','c++'],
    'tim' : ['c','java'],
    'eric' : ['java','rust'],
    'harry' : ['c++' , 'rust']
}

for names, languages in favourite_laguage.items():
    print(f"{names.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


users={
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton'
    },

    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris'
    }
}

for user_name, user_info in users.items():
    print(f"Username: {user_name}")
    full_name=f"{user_info['first']}{user_info['last']}"
    location=f"{user_info['location']}"
    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")