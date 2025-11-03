from pathlib import Path

path = Path('python/txt/programming.txt')

#path.write_text("I love Python.")

contents = "I love programming!\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path.write_text(contents)