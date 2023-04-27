from tkinter import*
from tkinter import ttk

root=Tk()
root.title('Mentālā veselība')
garums=800 #x
platums=500 #y
a=Canvas(root,width=garums,height=platums,bg='#4d4dff')
a.pack()
infocanva=Canvas(root,width=garums,height=platums,bg='#4d4dff')
infocanva.pack_forget()
Charimg=PhotoImage(file="image.png")
char=a.create_image(600,250,image=Charimg)

virsraksts2=infocanva.create_text(400,50,text="Mentālā veselība",fill="#660066",font=('Helvetica',30))
go_back=infocanva.create_text(700,480,text="Atgriezties",fill="#660066",font=('Helvetica',20))
info1=infocanva.create_text(400,140,text="Šī spēle ir par mentālo veselību",fill="#660066",font=('Helvetica',20))
info2=infocanva.create_text(380,200,text="Šajā spelē parādīts kā dažādi faktori ietekmē mentālo veselību",fill="#660066",font=('Helvetica',20))
info3=infocanva.create_text(400,270,text="Kā spēlēt?",fill="#660066",font=('Helvetica',20))
info3=infocanva.create_text(370,330,text="Mainot atbildes redzēsi, kā faktori ietekmē mentālo veselību",fill="#660066",font=('Helvetica',20))
info4=infocanva.create_text(400,370,text="un šo faktoru sekas",fill="#660066",font=('Helvetica',20))

virsraksts=a.create_text(400,50,text="Mentālā veselība",fill="#660066",font=('Helvetica',30))
Apgalvojums1=a.create_text(125,125,text="Cik daudz gulēji?",fill="#660066",font=('Helvetica',20))
Apgalvojums2=a.create_text(200,210,text="Cik daudz vingro katru dienu?",fill="#660066",font=('Helvetica',20))
Apgalvojums3=a.create_text(190,295,text="Kāds ir tavs stresa līmenis?",fill="#660066",font=('Helvetica',20))
Apgalvojums4=a.create_text(165,375,text="Kā tev patīk sava vide?",fill="#660066",font=('Helvetica',20))
info_bt=a.create_text(700,480,text="Informācija",fill="#660066",font=('Helvetica',20))

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# slider value
current_value1 = DoubleVar()
current_value2 = DoubleVar()
current_value3 = DoubleVar()
current_value4= DoubleVar()

def go_to_info():
    a.pack_forget()
    infocanva.pack()
def go_to_game():
    a.pack()
    infocanva.pack_forget()

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

#  slider
slider1 = ttk.Scale(root,from_=0,to=12,length=150,orient='horizontal',command=slider_changed,variable=current_value1)
slider1.pack()
a.create_window(125, 175, window=slider1)

slider2 = ttk.Scale(root,from_=0,to=12,length=150,orient='horizontal',command=slider_changed,variable=current_value2)
slider2.pack()
a.create_window(125, 260, window=slider2)

slider3 = ttk.Scale(root,from_=0,to=12,length=150,orient='horizontal',command=slider_changed,variable=current_value3)
slider3.pack()
a.create_window(125, 335, window=slider3)

slider4 = ttk.Scale(root,from_=0,to=12,length=150,orient='horizontal',command=slider_changed,variable=current_value4)
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


style = ttk.Style(root)

# Progressbar style
style.configure('my.Vertical.TProgressbar', background='#f7f4bf', troughcolor='#8a7852',pbarrelief='flat', troughrelief='flat')

pbar1 = ttk.Progressbar(root, maximum=12, value=get_current_value1(), orient='vertical', style='my.Vertical.TProgressbar')
pbar1.pack(side=LEFT)
pbar2 = ttk.Progressbar(root, maximum=12, value=get_current_value2(), orient='vertical', style='my.Vertical.TProgressbar')
pbar2.pack(side=LEFT)
pbar3 = ttk.Progressbar(root, maximum=12, value=get_current_value3(), orient='vertical', style='my.Vertical.TProgressbar')
pbar3.pack(side=LEFT)
pbar4 = ttk.Progressbar(root, maximum=12, value=get_current_value4(), orient='vertical', style='my.Vertical.TProgressbar')
pbar4.pack(side=LEFT)

a.tag_bind(info_bt,'<Button-1>', lambda event: go_to_info())
infocanva.tag_bind(go_back,'<Button-1>', lambda event: go_to_game())

root.configure()
root.mainloop()