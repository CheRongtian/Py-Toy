favourite_languages={
    'jen':'java',
    'tim':'python',
    'oliver':'c',
    'eric':'rust',
    'jeff':'c'
}
language = favourite_languages['eric'].title()
print(f"Eric's favourite language is {language}.")

point_value = favourite_languages.get('chris','he is not listed!').title()
#get() to check if the key is exist or not,
#if not, the following content would be expressed
# otherwise the value would be expressed 
print(point_value)

point_value2 = favourite_languages.get('tim','He is listed.').title()
print(point_value2)

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.\n")

for name in sorted(favourite_languages.keys()):#sorted list elements in a particular order
    print(f"{name.title()} is listed.")

for language in sorted(favourite_languages.values()):
    print(f"{language.title()}")

for language in set(favourite_languages.values()):# show the unique items
    print(f"{language}\n")