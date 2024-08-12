# Learning GUIs in Python!

from tkinter import *
import random


def main():
    root = Tk()

    def button():
        sides = ["right", "left", "bottom", "top"]
        colours = ["blue", "red", "yellow", "purple"]
        random_side = random.choice(sides)
        random_colour = random.choice(colours)
        random_colour_bg = random.choice(colours)

        click.pack(side=random_side)
        click.config(fg=random_colour, bg=random_colour_bg)

    click = Button(root, text="Click me! ", fg="red", command=button, pady=20, padx=50)
    click.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
