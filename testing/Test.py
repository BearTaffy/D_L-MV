from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

style = {'troughcolor': '#505050', 'sliderlength': 30, 'sliderrelief': 'flat', 'background': '#F0F0F0'}

scale = Scale(root, from_=0, to=12, orient=HORIZONTAL, length=200, **style)
scale.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
scale.place(x=100, y=100)

canvas.create_window(200, 200, window=scale)


scale.config(showvalue=True, sliderlength=20)
scale.bind('<Button-1>',)
scale.set(6)

root.mainloop()
