def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
#A function doesn't always gabe to display its output directly.
#Instead, it can process some data and then return a value or set of values.

musician = get_formatted_name('rongtian','che')
print(musician)
