from tkinter import*
from tkinter import ttk

root=Tk()
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
current_value = DoubleVar()


def get_current_value():
    return int(current_value.get())


def slider_changed(event):
    value_label.configure(text=get_current_value())
    pbar1.configure(value=get_current_value())

#  slider
slider = ttk.Scale(root,from_=0,to=12,orient='horizontal',command=slider_changed,variable=current_value).pack()



# value label
value_label = ttk.Label(root,text=get_current_value())



style = ttk.Style(root)

# Progressbar style
style.configure('my.Vertical.TProgressbar', background='#f7f4bf', troughcolor='#8a7852',pbarrelief='flat', troughrelief='flat')

pbar1 = ttk.Progressbar(root, maximum=12, value=get_current_value(), orient='vertical', style='my.Vertical.TProgressbar')



root.configure()
root.mainloop()
