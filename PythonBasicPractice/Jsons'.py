from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
number = json.loads(contents)
#json.loads() take in a JSON-formatted string and returns a python object which we assign to numbers

print(number)