from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding = 'utf-8',errors = 'ignore')
    except FileNotFoundError:
        pass
       #print(f"Sorry, the file {path} does not exist.")
       #try different outcomes here
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has {num_words} words.")

file_names = ['python/txt/pi1.txt', 'python/txt/BriefIntro.txt', 'python/txt/programming.txt','python/txt/one-million.txt']

for file_name in file_names:
    path = Path(file_name)
    count_words(path)