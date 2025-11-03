from pathlib import Path

path = Path("python/txt/BriefIntro.txt")
try:
    contents = path.read_text(encoding='utf-8',errors='ignore')
    #errors = 'ignore' is required here
    #otherwise it would show that 'utc-8' codec can't decode byte 0xd0 in position19: invalid continuation byte
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")