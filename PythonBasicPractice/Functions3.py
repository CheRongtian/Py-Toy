def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician1 = get_formatted_name('tim','jackson','robin')
print(musician1)
musician2 = get_formatted_name('tim','jackson')
print(musician2)

def build_person(first_name, last_name):
    person={'first':first_name,
            'last':last_name
            }
    return person

musician = build_person('jimi','pie')
print(musician)