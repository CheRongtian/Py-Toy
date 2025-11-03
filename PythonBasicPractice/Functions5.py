def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)



unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_designs = []
'''
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design.title()}")
    completed_designs.append(current_design)

print("\nThe following models have been printed:")
for completed_design in completed_designs:
    print(completed_design.title())
'''


def print_models(unprinted_designs, completed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"\nPrinting model: {current_design.title()}")
        completed_designs.append(current_design)

def show_completed_models(completed_designs):
    print("\nThe following models have been printed:")
    for completed_design in completed_designs:
        print(completed_design.title())

print_models(unprinted_designs, completed_designs)
show_completed_models(completed_designs)