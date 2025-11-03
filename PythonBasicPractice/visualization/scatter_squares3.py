import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x_value ** 2 for x_value in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap = plt.cm.Reds ,s = 10)
                                            #color = red/(0,0.8,0)
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

ax.tick_params(labelsize = 14)

#set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style = 'plain')

plt.savefig('squares_plot.png', bbox_inches = 'tight')
#plt.show()
 
