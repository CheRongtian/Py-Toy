requested_topping=['mushroom','pepper','bacon']
if 'mushroom' in requested_topping:
    print("Add mushroom, plz.")
if 'extra cheese' in requested_topping:
    print("Add extra cheese, plz.")

for toppings in requested_topping:
    if toppings == 'pepper':
        print("Sorry, pepper is sold out today.")
    else:
        print(f"We have those toppings listed: {toppings}.")

requests=[]#check if the lisi is empty or not.

if requests:
    for request in requests:
        print(f"Add {request}, plz.")

else:
    print("Do you want a plain pizza?")