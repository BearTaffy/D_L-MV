from tkinter import*

root=Tk()
root.title("Mentālā veselība")
garums=800 #x
platums=500 #y
a=Canvas(root,width=garums,height=platums,bg="#4d4dff")
a.pack()
infocanva=Canvas(root,width=garums,height=platums,bg="#4d4dff")
infocanva.pack_forget()
gamecanva=Canvas(root,width=garums,height=platums,bg="#4d4dff")
gamecanva.pack_forget()
bar_width = 0

# info canva
virsraksts2=infocanva.create_text(400,50,text="Mentālā veselība",fill="#660066",font=("Helvetica",30))
go_back=infocanva.create_text(700,480,text="Atgriezties",fill="#660066",font=("Helvetica",20))
#info1=infocanva.create_text(400,140,text="Šī spēle ir par mentālo veselību",fill="#660066",font=("Helvetica",20))
#info2=infocanva.create_text(380,200,text="Šajā spelē parādīts kā dažādi faktori ietekmē mentālo veselību",fill="#660066",font=("Helvetica",20))
#info3=infocanva.create_text(400,270,text="Kā spēlēt?",fill="#660066",font=("Helvetica",20))
#info3=infocanva.create_text(370,330,text="Mainot atbildes redzēsi, kā faktori ietekmē mentālo veselību",fill="#660066",font=("Helvetica",20))
#info4=infocanva.create_text(400,370,text="un šo faktoru sekas",fill="#660066",font=("Helvetica",20))
rs = infocanva.create_text(400,200, text="Šī spēle ir par mentālo veselību. Šajā spelē parādīts kā dažādi faktori ietekmē mentālo veselību.                     Kā spēlēt?             Mainot atbildes redzēsi, kā faktori ietekmē mentālo veselību un šo faktoru sekas.",width=400, fill="white",font=("helvetica",20))

# home canva
virsraksts=a.create_text(400,50,text="Mentālā veselība",fill="#660066",font=("Helvetica",30))
Apgalvojums1=a.create_text(125,125,text="Cik daudz gulēji?",fill="#660066",font=("Helvetica",20))
Apgalvojums2=a.create_text(200,210,text="Cik daudz vingro katru dienu?",fill="#660066",font=("Helvetica",20))
Apgalvojums3=a.create_text(190,295,text="Kāds ir tavs stresa līmenis?",fill="#660066",font=("Helvetica",20))
Apgalvojums4=a.create_text(165,375,text="Kā tev patīk sava vide?",fill="#660066",font=("Helvetica",20))
info_bt=a.create_text(700,480,text="Informācija",fill="#660066",font=("Helvetica",20))
game_bt=a.create_text(680,450,text="Redzēt rezultātus",fill="#660066",font=("Helvetica",20))

# game canva
go_back_home=gamecanva.create_text(650,480,text="Atpakaļ uz jautājumiem",fill="#660066",font=("Helvetica",20))

def callback(event):
    print( "clicked at", event.x, event.y)

a.bind("<Button-1>", callback)

def go_to_info():
    a.pack_forget()
    infocanva.pack()
def go_to_home():
    a.pack()
    infocanva.pack_forget()
def go_to_game():
    gamecanva.pack()
    a.pack_forget()
def go_to_home_from_game():
     gamecanva.pack_forget()
     a.pack()

def update_bar(event):
    global bar_width
    value = slider1.get()
    bar_width = value * 15
    a.coords(bar,240, 170, 240 + bar_width, 190)

def update_bar2(event):
    global bar_width
    value = slider2.get()
    bar_width = value * 15
    a.coords(bar2,240, 260, 240 + bar_width, 280)

def update_bar3(event):
    global bar_width
    value = slider3.get()
    bar_width = value * 15
    a.coords(bar3,240, 335, 240 + bar_width, 355)

def update_bar4(event):
    global bar_width
    value = slider4.get()
    bar_width = value * 15
    a.coords(bar4,240, 420, 240 + bar_width, 440)    

style = {"troughcolor": "#505050", "sliderlength": 30, "sliderrelief": "flat", "background": "#4d4dff"}


#  sliders

slider1 = Scale(root, from_=0, to=12, orient=HORIZONTAL, length=200, **style)
slider1.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
slider1.place(x=100, y=100)
a.create_window(125, 175, window=slider1)
slider1.config(showvalue=True, sliderlength=20,)
slider1.set(6)

slider2 = Scale(root, from_=0, to=12, orient=HORIZONTAL, length=200, **style)
slider2.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
slider2.place(x=100, y=100)
a.create_window(125, 260, window=slider2)
slider2.config(showvalue=True, sliderlength=20,)
slider2.set(6)

slider3 = Scale(root, from_=0, to=12, orient=HORIZONTAL, length=200, **style)
slider3.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
slider3.place(x=100, y=100)
a.create_window(125, 335, window=slider3)
slider3.config(showvalue=True, sliderlength=20,)
slider3.set(6)

slider4 = Scale(root, from_=0, to=12, orient=HORIZONTAL, length=200, **style)
slider4.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
slider4.place(x=100, y=100)
a.create_window(125, 420, window=slider4)
slider4.config(showvalue=True, sliderlength=20,)
slider4.set(6)




# Progressbars
bar = a.create_rectangle(240, 175, 240 + bar_width, 170, fill='white', outline='')
bar2= a.create_rectangle(240, 260, 240 + bar_width, 260, fill='white', outline='')
bar3= a.create_rectangle(240, 335, 240 + bar_width, 335, fill='white', outline='')
bar4= a.create_rectangle(240, 420, 240 + bar_width, 420, fill='white', outline='')
slider1.bind('<B1-Motion>', update_bar)
slider2.bind('<B1-Motion>', update_bar2)
slider3.bind('<B1-Motion>', update_bar3)
slider4.bind('<B1-Motion>', update_bar4)
# Buttons that move from one canvas to another canvas
a.tag_bind(info_bt,"<Button-1>", lambda event: go_to_info())
infocanva.tag_bind(go_back,"<Button-1>", lambda event: go_to_home())
a.tag_bind(game_bt,"<Button-1>",lambda event: go_to_game())
gamecanva.tag_bind(go_back_home,"<Button-1>",lambda event: go_to_home_from_game())

root.configure()
root.mainloop()