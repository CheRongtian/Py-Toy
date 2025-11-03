import plotly.express as px
from die import Die

#create a D6 and D10
D6 = Die()
D10 = Die(10)
#make some rolls, ans store results in a list
results = []

for roll_num in range(50_000):
    result = D6.roll() + D10.roll()
    results.append(result)

#analyze the results
frequencies = []
max_result = D6.num_sides + D10.num_sides
poss_results = range(1, max_result + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize the results
title = "Results of Rolling A D6 and A D10 50,000 Times"
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)

#further customize chart
fig.update_layout(xaxis_dtick = 1)

fig.show()
#fig.write_html('dice_visual_d6d10.html) #to save the figure, use this line to replace fig.show()