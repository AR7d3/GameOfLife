from os import pardir
from tkinter import *
import backend
import random

is_running = False
cell_size = 7
color = ['white']


def setup():
    global root, grid_view, cell_size, start_button, clear_button, choice, red_button, colorchoice

    root = Tk()
    root.resizable(False, False)
    root.configure(bg='#252526')
    root.title('The game of Life')
    mainlabel = Label(root, text="The Game of Life",
                      fg='white', background='#252526', font='Verdana 50 bold')
    grid_view = Canvas(root, width=backend.width*cell_size,
                       height=backend.height*cell_size,
                       borderwidth=0,
                       highlightthickness=1,
                       highlightbackground='gray',
                       bg='#1E1E1E')
    grid_view.bind('<B1-Motion>', grid_handler)

    start_button = Button(root, text='Start',
                          command=start_handler, highlightbackground='#252526')
    clear_button = Button(root, text='Clear',
                          command=clear_handler, highlightbackground='#252526')
    random_button = Button(
        root, text='Random', command=random_handler, highlightbackground='#252526')
    labelcolor = Label(root, text='Choose Color:', fg='white',
                       background='#252526')
    colorchoice = StringVar(root)
    colorchoice.set('white')
    coloroption = OptionMenu(root, colorchoice, 'white', 'red', 'blue',
                             'yellow', 'green', 'lime', 'orange', 'cyan', 'multicolor', command=pickcolor)
    coloroption.config(width=10, background='#252526')

    mainlabel.grid(row=0, columnspan=3, padx=(50, 0))
    grid_view.grid(row=1, columnspan=3, padx=(50, 0))
    start_button.grid(row=2, column=0, padx=(50, 0))
    random_button.grid(row=2, column=2, padx=(50, 0))
    clear_button.grid(row=2, column=1, padx=(50, 0))
    coloroption.grid(row=1, column=5, padx=(10, 10))
    labelcolor.grid(row=1, column=4, padx=(10, 0))


def random_handler():
    backend.grid_model = backend.randomize(backend.height, backend.width)
    update()


def pickcolor(event):
    global colorchoice, color
    if colorchoice.get() == 'multicolor':
        color = ['white', 'red', 'blue', 'yellow',
                 'green', 'lime', 'orange', 'cyan']
    else:
        color = [colorchoice.get()]


def start_handler():
    global is_running, start_button

    if is_running:
        is_running = False
        start_button.configure(text='Start')

    else:
        is_running = True
        start_button.configure(text='Pause')
        update()


def grid_handler(event):
    global grid_view, cell_size, color

    x = int(event.x/cell_size)
    y = int(event.y/cell_size)

    if (backend.grid_model[x][y] == 1):
        backend.grid_model[x][y] = 0
        draw_cell(x, y, '#1E1E1E')
    else:
        backend.grid_model[x][y] = 1
        draw_cell(x, y, random.choice(color))


def clear_handler():
    global is_running, start_button

    is_running = False
    for i in range(0, backend.height):
        for j in range(0, backend.width):
            backend.grid_model[i][j] = 0

    start_button.configure(text='Start')
    update()


def update():
    global grid_view, root, is_running, color
    grid_view.delete(ALL)
    backend.next_gen()

    for i in range(0, backend.height):
        for j in range(0, backend.width):
            if backend.grid_model[i][j] == 1:
                draw_cell(i, j, random.choice(color))
    if is_running:
        root.after(100, update)


def draw_cell(row, col, c):
    global grid_view, cell_size
    if c == '#1E1E1E':
        outline = '#1E1E1E'
    else:
        outline = 'gray24'
    grid_view.create_rectangle(row*cell_size, col*cell_size, row*cell_size +
                               cell_size, col*cell_size+cell_size, fill=c, outline=outline)


if __name__ == '__main__':
    setup()
    update()
    mainloop()
