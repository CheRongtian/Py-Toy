import plotly.express as px
from die import Die

#create a D6
D6 = Die()
#make some rolls, ans store results in a list
results = []

for roll_num in range(1000):
    result = D6.roll()
    results.append(result)

print(results)

#analyze the results
frequencies = []
poss_results = range(1, D6.num_sides + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#visualize the results
title = "Results of Rolling One D6 1,000 Times"
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
fig.show()