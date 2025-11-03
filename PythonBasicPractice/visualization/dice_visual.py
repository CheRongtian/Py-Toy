import plotly.express as px
from die import Die

#create 2 D6
D6_1 = Die()
D6_2 = Die()
#make some rolls, ans store results in a list
results = []

for roll_num in range(1000):
    result = D6_1.roll() + D6_2.roll()
    results.append(result)

#analyze the results
frequencies = []
max_result = D6_1.num_sides + D6_2.num_sides
poss_results = range(1, max_result + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize the results
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)

#further customize chart
fig.update_layout(xaxis_dtick = 1)

fig.show()