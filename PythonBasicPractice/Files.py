from pathlib import Path

path = Path('python/txt/pi.txt')
'''
contents = path.read_text()
contents = contents.rstrip()#remove the extra blank line
'''
contents = path.read_text().rstrip()
print(contents)