from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
#json.dumps() generate a string containing the JSON representation of the data we are working with
path.write_text(contents)