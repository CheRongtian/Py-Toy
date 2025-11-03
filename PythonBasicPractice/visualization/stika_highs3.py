from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('/Users/cherongtian/Desktop/python/visualization/death_valley_2018_simple.csv')
lines = path.read_text(encoding = 'utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#extract dates and high temperatures

dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[5])
    except ValueError:# for the error: invalid literal for int() with base 10
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)

#plot the high temperatures
plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
ax.plot(dates, highs, color = 'red')

#format plot
ax.set_title("Daily High Temperatures", fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Tenperature(F)", fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()