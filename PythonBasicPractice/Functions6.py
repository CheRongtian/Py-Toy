def make_pizza(*toppings):#arbitary arguements
    print(toppings)

make_pizza('mushroom', 'extra cheese', 'bacon')
make_pizza('beef')

def make_pizza2(*toppings):
    print("\n What kind of toppings do you want? ")
    for topping in toppings:
        print(f"-{topping.title()}")

make_pizza2('mushroom', 'extra cheese', 'bacon')
make_pizza2('beef')

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)
