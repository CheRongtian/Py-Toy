Man_Utd=['rashy','bruno','mainoo','mason']
print(Man_Utd)
print(Man_Utd[0].title())
print(Man_Utd[-1])
message = f"My favourite footballer in the club is {Man_Utd[-3].title()}."
print(message)

print(Man_Utd)

Man_Utd[-1]='harry'
print(Man_Utd)

Man_Utd.append('mason')
print(Man_Utd)

Man_Utd_Next_Season=[]
Man_Utd_Next_Season.append('mason mount')
Man_Utd_Next_Season.append('bruno fernandes')
Man_Utd_Next_Season.append('de ligt')
print(Man_Utd_Next_Season)

Man_Utd_Next_Season.insert(0,'harry maguire')
print(Man_Utd_Next_Season)

del Man_Utd_Next_Season[0]
print(Man_Utd_Next_Season)

poped_MU_Next_Season=Man_Utd_Next_Season.pop()
print(Man_Utd_Next_Season)
print(poped_MU_Next_Season)

Man_Utd_Next_Season.remove('bruno fernandes')
print(Man_Utd_Next_Season)