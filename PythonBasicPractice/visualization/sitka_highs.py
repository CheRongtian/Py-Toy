from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('/Users/cherongtian/Desktop/python/visualization/sitka_weather_07-2018_simple.csv')
lines = path.read_text(encoding = 'utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)
'''
for index, column_header in enumerate(header_row):
    print(index, column_header)
'''
#extract high temperatures
highs = []
for row in reader:
    high = int(row[5])
    highs.append(high)
print(highs)

#plot the high temperatures

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, color = 'red')

#format plot
ax.set_title("Daily High Temperatures", fontsize = 24)
ax.set_xlabel('', fontsize = 16)
ax.set_ylabel("Temperature(F)", fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()