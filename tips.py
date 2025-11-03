import tkinter as tk
import random
import time

def show_warm_tip(root):

    # create a window
    window = tk.Toplevel(root)

    # get size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # random window position
    window_width = 250
    window_height = 60
    x = random.randrange(0, screen_width - window_width)
    y = random.randrange(0, screen_height - window_height)

    # set title of window and position of window
    window.title('Tips')
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    tips = [
        'Hello1', 'Hello2', 'Hello3',
        'Hello4', 'Hello5', 'Hello6',
        'Hello7', 'Hello8', 'Hello9',
        'Hello10', 'Hello11', 'Hello12',
    ]

    tip = random.choice(tips)

    # background colour

    bg_colours = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender',
        'lightyellow', 'plum', 'coral', 'bisque', 'aquamarine',
        'mistyrose', 'honeydew', 'lavenderblush', 'oldlace'
    ]

    bg_color = random.choice(bg_colours)

    # set labels
    tk.Label(
        window,
        text=tip,
        bg=bg_color,
        font=('Arial', 16),
        width=30,
        height=5
    ).pack()

    window.attributes('-topmost', True)
    window.after(random.randint(400, 800), window.destroy)

root = tk.Tk()
root.withdraw()


# num of windows
for i in range(random.randint(5, 15)):
    root.after(i * 100, lambda: show_warm_tip(root)) 

root.after(2000, root.destroy)
root.mainloop()