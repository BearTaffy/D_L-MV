from tkinter import*
from tkinter import ttk

root=Tk()
style = ttk.Style(root)
root.title('Mentālā veselība')
garums=800
platums=500
a=Canvas(root,width=garums,height=platums,bg='#4d4dff')
a.pack()

virsraksts=a.create_text(400,50,text="Mentālā veselība",fill="#660066",font=('Helvetica',30))
Apgalvojums1=a.create_text(125,125,text="Cik daudz gulēji?",fill="#660066",font=('Helvetica',20))
Apgalvojums2=a.create_text(200,210,text="Cik daudz vingro katru dienu?",fill="#660066",font=('Helvetica',20))
Apgalvojums3=a.create_text(190,295,text="Kāds ir tavs stresa līmenis?",fill="#660066",font=('Helvetica',20))
Apgalvojums4=a.create_text(165,375,text="Kā tev patīk sava vide?",fill="#660066",font=('Helvetica',20))

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# slider value
current_value1 = DoubleVar()
current_value2 = DoubleVar()
current_value3 = DoubleVar()
current_value4= DoubleVar()

def get_current_value1():
    return int(current_value1.get())
def get_current_value2():
    return int(current_value2.get())
def get_current_value3():
    return int(current_value3.get())
def get_current_value4():
    return int(current_value4.get())


def slider_changed(event):
    value_label1.configure(text=get_current_value1())
    value_label2.configure(text=get_current_value2())
    value_label3.configure(text=get_current_value3())
    value_label4.configure(text=get_current_value4())
    pbar1.configure(value=get_current_value1())
    pbar2.configure(value=get_current_value2())
    pbar3.configure(value=get_current_value3())
    pbar4.configure(value=get_current_value4())

# Slider style
style.configure('horzontal_Slider', background='#4d4dff')


#  slider
slider1 = ttk.Scale(root,from_=0,to=12,length=150,orient='horizontal',command=slider_changed,variable=current_value1,style='horzontal_Slider')
slider1.pack()
a.create_window(125, 175, window=slider1)

slider2 = ttk.Scale(root,from_=0,to=12,length=150,orient='horizontal',command=slider_changed,variable=current_value2,style='horzontal_Slider')
slider2.pack()
a.create_window(125, 260, window=slider2)

slider3 = ttk.Scale(root,from_=0,to=12,length=150,orient='horizontal',command=slider_changed,variable=current_value3,style='horzontal_Slider')
slider3.pack()
a.create_window(125, 335, window=slider3)

slider4 = ttk.Scale(root,from_=0,to=12,length=150,orient='horizontal',command=slider_changed,variable=current_value4,style='horzontal_Slider')
slider4.pack()
a.create_window(125, 420, window=slider4)


# value label
value_label1 = ttk.Label(root,text=get_current_value1())
value_label2 = ttk.Label(root,text=get_current_value2())
value_label3 = ttk.Label(root,text=get_current_value3())
value_label4 = ttk.Label(root,text=get_current_value4())
value_label1.pack(side=LEFT)
value_label2.pack(side=LEFT)
value_label3.pack(side=LEFT)
value_label4.pack(side=LEFT)




# Progressbar style
style.configure('vertical_ProgressBar', background='#f7f4bf', troughcolor='#8a7852',pbarrelief='flat', troughrelief='flat')

pbar1 = ttk.Progressbar(root, maximum=12, value=get_current_value1(), orient='vertical', style='vertical_ProgressBar')
pbar1.pack(side=LEFT)
pbar2 = ttk.Progressbar(root, maximum=12, value=get_current_value2(), orient='vertical', style='vertical_ProgressBar')
pbar2.pack(side=LEFT)
pbar3 = ttk.Progressbar(root, maximum=12, value=get_current_value3(), orient='vertical', style='vertical_ProgressBar')
pbar3.pack(side=LEFT)
pbar4 = ttk.Progressbar(root, maximum=12, value=get_current_value4(), orient='vertical', style='vertical_ProgressBar')
pbar4.pack(side=LEFT)


root.configure()
root.mainloop()