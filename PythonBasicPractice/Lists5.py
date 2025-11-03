footballers=['harry','bruno','mason','kobe','rashy']
print(footballers[0:3])
print(footballers[:3])
print(footballers[3:])
print(footballers[-2:])

print("Here is my favourite footballer in the club: ")
for footballer in footballers[:2]:
    print(footballer.title())

mu_lineup=footballers[:] #copy the line
print(mu_lineup)