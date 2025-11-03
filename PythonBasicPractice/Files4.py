from pathlib import Path

path = Path('python/txt/one-million.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))