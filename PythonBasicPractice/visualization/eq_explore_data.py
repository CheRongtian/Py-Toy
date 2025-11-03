from pathlib import Path
import json

#read data as string and convert to a python object

path = Path('visualization/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#create a more readable version of the date file
path = Path('visualization/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent = 4)
path.write_text(readable_contents)