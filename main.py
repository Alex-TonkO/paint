from tkinter.colorchooser import *
from tkinter import *

from data import config as c
from data.setup import load_image

brush_size = c.BRUSH_SIZE
color = c.DEFAULT_COLOR


def draw(event):
    x1 = event.x - brush_size
    y1 = event.y - brush_size
    x2 = event.x + brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def active_paint(event):
    global brush_size
    global color
    w.bind("<B1-Motion>", draw)
    w.bind("<ButtonPress-1>", draw)


def decrease_brush_size():
    global brush_size
    if brush_size > 5:
        brush_size -= 1


def increase_brush_size():
    global brush_size
    if brush_size < 20:
        brush_size += 1


def color_change(new_color):
    global color
    color = new_color


def get_color():
    global color
    color = askcolor(title="Colors")
    color_change(color[1])


root = Tk()
root.title("Paint")

w = Canvas(root, width=c.WIDTH, height=c.HEIGHT, bg=c.BG_COLOR)
w.bind("<1>", active_paint)
eraser_icon = load_image('eraser.png')
increase_icon = load_image('inbrush.png')
decrease_icon = load_image('debrush.png')
brush_icon = load_image('brush.png')
eraser_btn = Button(image=eraser_icon, command=lambda: color_change("#ffffff"))  # 111111
decrease_btn = Button(image=decrease_icon, command=decrease_brush_size)
increase_btn = Button(image=increase_icon, command=increase_brush_size)
brush_btn = Button(image=brush_icon, command=lambda: color_change(c.DEFAULT_COLOR))
remove_all_btn = Button(text="Remove all", width=10, command=lambda: w.delete("all"))

blanched_almond_btn = Button(bg="#FFF1C9", width=2, command=lambda: color_change("#FFF1C9"))
melon_btn = Button(bg="#F7B7A3", width=2, command=lambda: color_change("#F7B7A3"))
water_mellon_btn = Button(bg="#EA5F89", width=2, command=lambda: color_change("#EA5F89"))
violet_btn = Button(bg="#9B3192", width=2, command=lambda: color_change("#9B3192"))
dark_purple_btn = Button(bg="#2B0B3F", width=2, command=lambda: color_change("#2B0B3F"))
alien_armpit_btn = Button(bg='#89DF00', width=2, command=lambda: color_change('#89DF00'))
spring_bud_btn = Button(bg='#A1F500', width=2, command=lambda: color_change('#A1F500'))
magic_mint_btn = Button(bg='#ADFFB9', width=2, command=lambda: color_change('#ADFFB9'))
medium_spring_green_btn = Button(bg='#00F798', width=2, command=lambda: color_change('#00F798'))
green_btn = Button(bg='#10B56F', width=2, command=lambda: color_change('#10B56F'))
picker_btn = Button(text="Color all", width=10, command=get_color)

w.grid(row=2, column=3, rowspan=50, columnspan=50, sticky=W + E + N + S, padx=5, pady=5)
decrease_btn.grid(row=1, column=5)
increase_btn.grid(row=1, column=6)
brush_btn.grid(row=1, column=7)
eraser_btn.grid(row=1, column=8)
remove_all_btn.grid(row=1, column=9)

blanched_almond_btn.grid(row=2, column=1)
melon_btn.grid(row=3, column=1)
water_mellon_btn.grid(row=4, column=1)
violet_btn.grid(row=5, column=1)
dark_purple_btn.grid(row=6, column=1)
alien_armpit_btn.grid(row=2, column=2)
spring_bud_btn.grid(row=3, column=2)
magic_mint_btn.grid(row=4, column=2)
medium_spring_green_btn.grid(row=5, column=2)
green_btn.grid(row=6, column=2)
picker_btn.grid(row=7, columnspan=3)

mainloop()
