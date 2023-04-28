from tkinter import*

root=Tk()
garums=800 
platums=500 
canvas=Canvas(root,width=garums,height=platums)
canvas.pack()

virsraksts=canvas.create_text(400,50,text="Mentālā veselība",font=("Helvetica",30))

Apgalvojums1=canvas.create_text(125,125,text="Cik daudz gulēji?",font=("Helvetica",20))

def update_bar(event):
    global bar_width
    value = scale.get()
    bar_width = value * 15
    canvas.coords(bar,200, 250, 200 + bar_width, 270)

bar_width = 0
bar = canvas.create_rectangle(240, 290, 240 + bar_width, 310, fill='#4d4dff', outline='')


style = {"troughcolor": "#505050", "sliderlength": 30, "sliderrelief": "flat", "background": "#4d4dff"}
scale = Scale(root, from_=0, to=12, orient=HORIZONTAL, length=200, **style)
scale.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
scale.place(x=100, y=100)
canvas.create_window(125, 175, window=scale)
scale.config(showvalue=True, sliderlength=20,)
scale.set(6)


scale.bind('<B1-Motion>', update_bar)
root.configure()
root.mainloop()