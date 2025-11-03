from pathlib import Path
import json

path = Path('/Users/cherongtian/Desktop/python/visualization/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)


all_eq_dicts = all_eq_data['features']
'''
print(len(all_eq_dicts))#examine all earthquakes in the dataset
'''

'''
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    #each earthquake's magnitude is stored in the 'properties' section of this dictionary, under the key 'mag'
    mags.append(mag)
print(mags[:10])
'''

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])