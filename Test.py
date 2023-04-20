from tkinter import *

from tkinter import ttk



# root window
root = Tk()
root.geometry('600x300')
root.resizable(False, False)



root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# slider value
current_value = DoubleVar()


def get_current_value():
    return int(current_value.get())

def done():
    pbar1 = ttk.Progressbar(root, maximum=12, value=get_current_value(), orient='vertical', style='my.Vertical.TProgressbar')
    pbar1.grid(row=2, column=0, padx=40, pady=10)


def slider_changed(event):
    value_label.configure(text=get_current_value())
    pbar1.configure(value=get_current_value())

#  slider
slider = ttk.Scale(root,from_=0,to=12,orient='horizontal',command=slider_changed,variable=current_value)

slider.grid(column=0,row=0,sticky='we')

# value label
value_label = ttk.Label(root,text=get_current_value())
value_label.grid(row=1,columnspan=1,sticky='n')

dutton = ttk.Button(root,text="save",command=done())
dutton.grid(column=5,row=4,sticky='se')

style = ttk.Style(root)

# Progressbar style
style.configure('my.Vertical.TProgressbar', background='#f7f4bf', troughcolor='#8a7852',pbarrelief='flat', troughrelief='flat')

pbar1 = ttk.Progressbar(root, maximum=12, value=get_current_value(), orient='vertical', style='my.Vertical.TProgressbar')
pbar1.grid(row=2, column=0, padx=40, pady=10)


root.configure()
root.mainloop()
