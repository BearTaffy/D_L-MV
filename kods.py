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
sleep1=gamecanva.create_text(50,50,text="Miegs")
gym1=gamecanva.create_text(50,75,text="Vingrošana")
stress1=gamecanva.create_text(50,100,text="Stress")
vide1=gamecanva.create_text(50,125,text="Vide")
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

slider3 = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=200, **style)
slider3.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
slider3.place(x=100, y=100)
a.create_window(125, 335, window=slider3)
slider3.config(showvalue=True, sliderlength=20,)
slider3.set(6)

slider4 = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=200, **style)
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
# Hideing the progressbars
a.itemconfigure(bar,state="hidden")
a.itemconfigure(bar2,state="hidden")
a.itemconfigure(bar3,state="hidden")
a.itemconfigure(bar4,state="hidden")
# Buttons that move from one canvas to another canvas
a.tag_bind(info_bt,"<Button-1>", lambda event: go_to_info())
infocanva.tag_bind(go_back,"<Button-1>", lambda event: go_to_home())
a.tag_bind(game_bt,"<Button-1>",lambda event: go_to_game())
gamecanva.tag_bind(go_back_home,"<Button-1>",lambda event: go_to_home_from_game())
# Buttons that show the results
gamecanva.tag_bind(sleep1,"<Button-1>",lambda event: sleep())
gamecanva.tag_bind(gym1,"<Button-1>",lambda event: gym())
gamecanva.tag_bind(stress1,"<Button-1>",lambda event: stress())
gamecanva.tag_bind(vide1,"<Button-1>",lambda event: vide())

root.configure()
root.mainloop()