from tkinter import*

root=Tk()
root.title("Mentālā veselība")
garums=800 #x
platums=700 #y
a=Canvas(root,width=garums,height=platums,bg="#b366ff")
a.pack()
infocanva=Canvas(root,width=garums,height=platums,bg="#b366ff")
infocanva.pack_forget()
gamecanva=Canvas(root,width=garums,height=platums,bg="#b366ff")
gamecanva.pack_forget()
bar_width = 0

# info canva
virsraksts2=infocanva.create_text(400,50,text="Mentālā veselība",fill="#660066",font=("Helvetica",30))
go_back=infocanva.create_text(700,platums-20,text="Atgriezties",fill="#660066",font=("Helvetica",20))
#info1=infocanva.create_text(400,140,text="Šī spēle ir par mentālo veselību",fill="#660066",font=("Helvetica",20))
#info2=infocanva.create_text(380,200,text="Šajā spelē parādīts kā dažādi faktori ietekmē mentālo veselību",fill="#660066",font=("Helvetica",20))
#info3=infocanva.create_text(400,270,text="Kā spēlēt?",fill="#660066",font=("Helvetica",20))
#info3=infocanva.create_text(370,330,text="Mainot atbildes redzēsi, kā faktori ietekmē mentālo veselību",fill="#660066",font=("Helvetica",20))
#info4=infocanva.create_text(400,370,text="un šo faktoru sekas",fill="#660066",font=("Helvetica",20))
rs = infocanva.create_text(400,200, text="Šī spēle ir par mentālo veselību. Šajā spelē parādīts kā dažādi faktori ietekmē mentālo veselību. Kā spēlēt? Mainot atbildes redzēsi, kā faktori ietekmē mentālo veselību un šo faktoru sekas.",width=400, fill="white",font=("helvetica",20))

# home canva
virsraksts=a.create_text(400,50,text="Mentālā veselība",fill="#660066",font=("Helvetica",30))
Apgalvojums1=a.create_text(125,125,text="Cik daudz gulēji?",fill="#660066",font=("Helvetica",20))
Apgalvojums2=a.create_text(190,210,text="Vai tu vingro katru dienu?",fill="#660066",font=("Helvetica",20))
Apgalvojums2_ja=a.create_text(90,240,text="Jā",fill="#660066",font=("Helvetica",20))
Apgalvojums2_ne=a.create_text(180,240,text="Nē",fill="#660066",font=("Helvetica",20))
Apgalvojums3=a.create_text(190,320,text="Kāds ir tavs stresa līmenis?",fill="#660066",font=("Helvetica",20))
Apgalvojums4=a.create_text(165,400,text="Kā tev patīk sava vide?",fill="#660066",font=("Helvetica",20))
Apgalvojums5=a.create_text(290,530,text="Cik daudz laika(stundas) ikdienā veltāt sociālajiem medijiem vai digitālajām ierīcēm?",fill="#660066",font=("Helvetica",20),width=600)
info_bt=a.create_text(700,platums-20,text="Informācija",fill="#660066",font=("Helvetica",20))
game_bt=a.create_text(680,platums-50,text="Redzēt rezultātus",fill="#660066",font=("Helvetica",20))

# game canva
go_back_home=gamecanva.create_text(650,platums-20,text="Atpakaļ uz jautājumiem",fill="#660066",font=("Helvetica",20))
sleep1=gamecanva.create_text(70,50,text="Miegs",fill="#660066",font=("Helvetica",20))
gym1=gamecanva.create_text(70,100,text="Vingrošana",fill="#660066",font=("Helvetica",20))
stress1=gamecanva.create_text(70,150,text="Stress",fill="#660066",font=("Helvetica",20))
vide1=gamecanva.create_text(70,200,text="Vide",fill="#660066",font=("Helvetica",20))
screen_time1=gamecanva.create_text(100,250,text="Digitālās ierīces",fill="#660066",font=("Helvetica",20))
def callback(event):
    print( "clicked at", event.x, event.y)

a.bind("<Button-1>", callback)
# Functions that move from one canvas to another
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

def update_bar5(event):
    global bar_width
    value = slider5.get()
    bar_width = value * 15
    a.coords(bar5,240, 420, 240 + bar_width, 440)   
# functions that show the slider for gym
def yes():
    a.itemconfigure(slidder2_s,state="normal")
def no():
    a.itemconfigure(slidder2_s,state="hidden")


# the functions that are the ones that show the results
def sleep():
    red1 = "Tu guli pārāk maz katru nakti, tev būtu jāguļ 7-9 stundas. Pārliecinieties, vai dienas laikā iegūstat pietiekami daudz saules gaismas, nedzer dzērienus, kuros ir kofeīnu, pārāk tuvu gulētiešanas laikam. Ekrāna laika ierobežošana pirms miega var arī palīdzēt samazināt miega problēmas."
    yellow1 = "Tu guli pārāk daudz tev būtu jāguļ 7-9 stundas. Tas var šķist vienkārši, bet viens, ko var darīt, ir ievērot noteiktu gulēšanas laiku un pamošanās laiku sev. Tas var palīdzēt ķermenim izveidot savu rutīnu, tādējādi palīdzot izvairīties no pārāk liela vai pārāk maza miega. Ja vēlies labāk izgulēties, būtiski ir pārliecināties, vai istabā ir tumšs. Lai ir klusums un arī telpas temperatūra ir jums patīkama. Ja ir par karstu vai par aukstu, tad izredzes, ka īpaši labi neizgulēsies."
    green1 = "Tu guli pietiekami daudz un nekas nav jāmaina. Tā turpini!"
    block = gamecanva.create_rectangle(550, 50, 750, 450, fill="white")
    if slider1.get() <= 6:
        sleep_tx = gamecanva.create_text(650, 250, text=red1, width=200, fill="black", font=("helvetica", 15))
    elif 7 <= slider1.get() <= 9:
        sleep_tx = gamecanva.create_text(650, 250, text=green1, width=200, fill="black", font=("helvetica", 15))
    elif 9 < slider1.get() <= 12:
        sleep_tx = gamecanva.create_text(650, 250, text=yellow1, width=200, fill="black", font=("helvetica", 12))

def gym():
    red2="Tu vingro par maz. Tev dienā vajag vingrot vismaz 30 minūtes. Vingrot var arī mājās bez speciāla inventāra."
    green2="Tu vingro pietiekami daudz! Tā turpini!"
    yellow2="Tu vingro ļoti daudz, esi uzmanīgs, lai nepārslogotu sevi."
    block = gamecanva.create_rectangle(550, 50, 750, 450, fill="white")
    if slider2.get() ==0:
        gym_tx = gamecanva.create_text(650, 250, text=red2, width=200, fill="black", font=("helvetica", 15))
    elif  slider2.get() <=1:
        gym_tx = gamecanva.create_text(650, 250, text=green2, width=200, fill="black", font=("helvetica", 15))
    elif 2< slider2.get() <= 12:
        gym_tx = gamecanva.create_text(650, 250, text=yellow2, width=200, fill="black", font=("helvetica", 15))

def stress():
    red3="Tev ir pārāk liels stress tev var būt sāpes krūtīs un paaugstināts asinsspiediens, gremošanas traucējumi. Esi aktīvs. Praktiski jebkura veida fiziskās aktivitātes var darboties kā stresa mazinātājs. Komunicē ar citiem, klausies nomierinošu mūziku."
    green3="Kad esat bez stresa, jūs bieži domājat daudz skaidrāk, esat labāk sagatavots, lai pieņemtu pareizos lēmumus, un jums ir daudz pozitīvāks skatījums uz apkārt notiekošo – gan darbā, gan mājās."
    yellow3="Esi aktīvs. Praktiski jebkura veida fiziskās aktivitātes var darboties kā stresa mazinātājs. Komunicē ar citiem, klausies nomierinošu mūziku."
    block = gamecanva.create_rectangle(550, 50, 750, 450, fill="white")
    if 7<=slider3.get() and slider3.get() <=10:
        stress_tx = gamecanva.create_text(650, 250, text=red3, width=200, fill="black", font=("helvetica", 15))
    elif 0== slider3.get() or slider3.get() <=2:
        stress_tx = gamecanva.create_text(650, 250, text=green3, width=200, fill="black", font=("helvetica", 15))
    elif 2== slider3.get() or slider3.get() <=6:
        stress_tx = gamecanva.create_text(650, 250, text=yellow3, width=200, fill="black", font=("helvetica", 15))

def vide():
    red4="Ja tev nepatīk sava vide. Tā ir jāmaina ar paša spēkiem vai ar citu palīdzību."
    green4="Tas ir labi, ka tev patīk sava vide. Tava vide tevi ļoti ietekmē, ja tev nepatīk sava vide tā var ietekmēt tavas mācības."
    yellow4="Skaties, ko tu vari uzlabot vai mainīt savā vidē, jo tai ir liels iespaids uz tevi."
    block = gamecanva.create_rectangle(550, 50, 750, 450, fill="white")
    if 7<=slider4.get() and slider4.get() <=10:
        stress_tx = gamecanva.create_text(650, 250, text=green4, width=200, fill="black", font=("helvetica", 15))
    elif 0== slider4.get() or slider4.get() <=2:
        stress_tx = gamecanva.create_text(650, 250, text=red4, width=200, fill="black", font=("helvetica", 15))
    elif 2== slider4.get() or slider4.get() <=6:
        stress_tx = gamecanva.create_text(650, 250, text=yellow4, width=200, fill="black", font=("helvetica", 15))

def screen_time():
    red5="Tev noteikti jāsamazina veltītais laiks ierīcēm! Tu pārsnied vidējo, kas ir septiņas stundas. Tu vari ierobežot savu laiku pieliekot sociālajiem tīkliem noteiktu laika limitu cik tos var izmantot vai arī sāc jaunu hobiju."
    green5="Tu vari lepoties ar savu atbildi, jo vidējais laiks cik pavada sociālajos tīklos un pie ierīču ekrāniem ir septiņas stundas dienā. "
    yellow5="Tev vajadzētu samazināt savu laiku sociālajos tīklos un pie ierīču ekrāniem, bet tu nepārsniedz septiņas stundas, kas ir cik vidēji cilvēks velta laiku ierīcēm."
    block = gamecanva.create_rectangle(550, 50, 750, 450, fill="white")
    if slider5.get()<=2:
        screen_time_tx = gamecanva.create_text(650, 250, text=green5, width=200, fill="black", font=("helvetica", 15))
    elif  2<slider5.get() and slider5.get() <=7:
        screen_time_tx = gamecanva.create_text(650, 250, text=yellow5, width=200, fill="black", font=("helvetica", 15))
    elif 7< slider5.get() and slider5.get() >=15:
        screen_time_tx = gamecanva.create_text(650, 250, text=red5, width=200, fill="black", font=("helvetica", 15))

style = {"troughcolor": "#505050", "sliderlength": 30, "sliderrelief": "flat", "background": "#b366ff"}



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
slidder2_s=a.create_window(125, 285, window=slider2)
slider2.config(showvalue=True, sliderlength=20,)
slider2.set(6)

slider3 = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=200, **style)
slider3.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
slider3.place(x=100, y=100)
a.create_window(125, 360, window=slider3)
slider3.config(showvalue=True, sliderlength=20,)
slider3.set(6)

slider4 = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=200, **style)
slider4.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
slider4.place(x=100, y=100)
a.create_window(125, 445, window=slider4)
slider4.config(showvalue=True, sliderlength=20,)
slider4.set(6)

slider5 = Scale(root, from_=0, to=15, orient=HORIZONTAL, length=200, **style)
slider5.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
slider5.place(x=100, y=100)
a.create_window(125, 580, window=slider5)
slider5.config(showvalue=True, sliderlength=20,)
slider5.set(6)




# Progressbars
bar = a.create_rectangle(240, 175, 240 + bar_width, 170, fill='white', outline='')
bar2= a.create_rectangle(240, 260, 240 + bar_width, 260, fill='white', outline='')
bar3= a.create_rectangle(240, 335, 240 + bar_width, 335, fill='white', outline='')
bar4= a.create_rectangle(240, 420, 240 + bar_width, 420, fill='white', outline='')
bar5= a.create_rectangle(240, 420, 240 + bar_width, 420, fill='white', outline='')
slider1.bind('<B1-Motion>', update_bar)
slider2.bind('<B1-Motion>', update_bar2)
slider3.bind('<B1-Motion>', update_bar3)
slider4.bind('<B1-Motion>', update_bar4)
slider5.bind('<B1-Motion>', update_bar5)
# Hideing the progressbars
a.itemconfigure(bar,state="hidden")
a.itemconfigure(bar2,state="hidden")
a.itemconfigure(bar3,state="hidden")
a.itemconfigure(bar4,state="hidden")
a.itemconfigure(bar5,state="hidden")
# hideing the gym slider
a.itemconfigure(slidder2_s,state="hidden")
# Buttons that move from one canvas to another canvas
a.tag_bind(info_bt,"<Button-1>", lambda event: go_to_info())
infocanva.tag_bind(go_back,"<Button-1>", lambda event: go_to_home())
a.tag_bind(game_bt,"<Button-1>",lambda event: go_to_game())
gamecanva.tag_bind(go_back_home,"<Button-1>",lambda event: go_to_home_from_game())
# Buttons that show and hide the gym slider
a.tag_bind(Apgalvojums2_ja,"<Button-1>",lambda event: yes())
a.tag_bind(Apgalvojums2_ne,"<Button-1>",lambda event: no())
# Buttons that show the results
gamecanva.tag_bind(sleep1,"<Button-1>",lambda event: sleep())
gamecanva.tag_bind(gym1,"<Button-1>",lambda event: gym())
gamecanva.tag_bind(stress1,"<Button-1>",lambda event: stress())
gamecanva.tag_bind(vide1,"<Button-1>",lambda event: vide())
gamecanva.tag_bind(screen_time1,"<Button-1>",lambda event: screen_time() )


root.configure()
root.mainloop()