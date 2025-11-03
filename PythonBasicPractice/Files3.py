from pathlib import Path

path = Path('python/txt/pi.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()#returns a list of all lines in the file
pi_string = ''
for line in lines:
    pi_string += line.lstrip()#get rid of the blanks

print(pi_string)
print(len(pi_string))