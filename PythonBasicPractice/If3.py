available_toppings=['mushroom','bacon','pepper','extra cheese','olives','pneapple']
request_toppings=['bacon','mushroom','french fries','double cheese']

for request_topping in request_toppings:
    if request_topping in available_toppings:
        print(f"Ok, we could offer {request_topping} for you.")
    elif request_topping == 'double cheese':
        print("How about extra cheese as an alternative?")
    else:
        print(f"Sorry, we do not have {request_topping} as a topping here.")

print("Thanks for your order.")