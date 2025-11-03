def greet_user(username):
    print(f"Hello! {username.title()}.")

name = input("\nEnter a name here: ")
greet_user(name)

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')# == describe(animal_type='hamster',pet_name='harry')
describe_pet('dog','willie')

