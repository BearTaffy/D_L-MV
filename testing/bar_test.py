from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

style = {'troughcolor': '#505050', 'sliderlength': 30, 'sliderrelief': 'flat', 'background': '#F0F0F0'}

scale = Scale(root, from_=0, to=12, orient=HORIZONTAL, length=200, **style)
scale.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
scale.place(x=100, y=100)

canvas.create_window(200, 200, window=scale)

bar_width = 0
bar = canvas.create_rectangle(100, 150, 100 + bar_width, 170, fill='#4d4dff', outline='')

def update_bar(event):
    global bar_width
    value = scale.get()
    bar_width = value * 15
    canvas.coords(bar, 100, 150, 100 + bar_width, 170)

scale.bind('<B1-Motion>', update_bar)

root.mainloop()

