from tkinter import*

root=Tk()
root.title("Mentālā veselība")

garums=800 #x
platums=700 #y

a=Canvas(root,width=garums,height=platums,bg="#4169E1")
a.pack()

infocanva=Canvas(root,width=garums,height=platums,bg="#4169E1")
infocanva.pack_forget()

gamecanva=Canvas(root,width=garums,height=platums,bg="#4169E1")
gamecanva.pack_forget()

bar_width = 0

mobings = 0

health_Head = 0
health_Body = 0
health_Legs = 0


img_head_green = PhotoImage(file="person/Head/head_green.png")
img_head_yellow = PhotoImage(file="person/Head/head_yellow.png")
img_head_red = PhotoImage(file="person/Head/head_Red.png")
img_head = PhotoImage(file="person/Head/head_normal.png")

img_body_green = PhotoImage(file="person/Body/body_green.png")
img_body_yellow = PhotoImage(file="person/Body/body_yellow.png")
img_body_red = PhotoImage(file="person/Body/body_Red.png")
img_body = PhotoImage(file="person/Body/body_normal.png")

img_legs_green = PhotoImage(file="person/Legs/legs_green.png")
img_legs_yellow = PhotoImage(file="person/Legs/legs_yellow.png")
img_legs_red = PhotoImage(file="person/Legs/legs_Red.png")
img_legs = PhotoImage(file="person/Legs/legs_normal.png")

# info canva
virsraksts2=infocanva.create_text(400,50,text="Mentālā veselība",fill="#CCCCCC",font=("Helvetica",30))
go_back=infocanva.create_text(700,platums-20,text="Atgriezties",fill="#CCCCCC",font=("Helvetica",20))
rs = infocanva.create_text(400,250, text="Šī spēle ir par mentālo veselību. Šajā spelē parādīts kā dažādi faktori ietekmē mentālo veselību.\n\nKā spēlēt?\nMainot atbildes redzēsi, kā faktori ietekmē mentālo veselību un šo faktoru sekas.",width=400, fill="white",font=("helvetica",20))

# home canva
virsraksts=a.create_text(400,50,text="Mentālā veselība",fill="#CCCCCC",font=("Helvetica",30))
Apgalvojums1=a.create_text(142,125,text="Cik stundas tu guli?",fill="#CCCCCC",font=("Helvetica",20))
Apgalvojums2=a.create_text(200,220,text="Cik stundas nedeļa tu vingro?",fill="#CCCCCC",font=("Helvetica",20))
Apgalvojums3=a.create_text(190,320,text="Kāds ir tavs stresa līmenis?",fill="#CCCCCC",font=("Helvetica",20))
Apgalvojums4=a.create_text(165,400,text="Kā tev patīk sava vide?",fill="#CCCCCC",font=("Helvetica",20))
Apgalvojums5=a.create_text(305,510,text="Cik stundas ikdienā veltāt digitālajām ierīcēm?",fill="#CCCCCC",font=("Helvetica",20))
Apgalvojums6=a.create_text(225,610,text="Vai pret tevi, kāds dara mobingu?",fill="#CCCCCC",font=("Helvetica",20))
Apgalvojums6_ja=a.create_text(90,660,text="Jā",fill="#CCCCCC",font=("Helvetica",20))
Apgalvojums6_ne=a.create_text(180,660,text="Nē",fill="#CCCCCC",font=("Helvetica",20))
info_bt=a.create_text(680,platums-20,text="Informācija",fill="#CCCCCC",font=("Helvetica",20))
game_bt=a.create_text(680,platums-50,text="Redzēt rezultātus",fill="#CCCCCC",font=("Helvetica",20))

# game canva
go_back_home=gamecanva.create_text(650,platums-20,text="Atpakaļ uz jautājumiem",fill="#CCCCCC",font=("Helvetica",20))
sleep1=gamecanva.create_text(70,50,text="Miegs",fill="#CCCCCC",font=("Helvetica",20))
gym1=gamecanva.create_text(100,100,text="Vingrošana",fill="#CCCCCC",font=("Helvetica",20))
stress1=gamecanva.create_text(70,150,text="Stress",fill="#CCCCCC",font=("Helvetica",20))
vide1=gamecanva.create_text(60,200,text="Vide",fill="#CCCCCC",font=("Helvetica",20))
screen_time1=gamecanva.create_text(128,250,text="Digitālās ierīces",fill="#CCCCCC",font=("Helvetica",20))
mobings1=gamecanva.create_text(85,300,text="Mobings",fill="#CCCCCC",font=("Helvetica",20))

def callback(event):
    print( "clicked at", event.x, event.y)

a.bind("<Button-1>", callback)
def score():
    global health_Head
    global health_Body
    global health_Legs
    health_Head = 0
    health_Body = 0
    health_Legs = 0
    #sleep
    if slider1.get() <= 2:
        health_Head -= 3
        health_Body -= 2
        health_Legs -= 2
    elif slider1.get() <= 4:
        health_Head -= 2
        health_Body -= 1
        health_Legs -= 1
    elif slider1.get() <= 6:
        health_Head -= 1
        health_Body -= 0
        health_Legs -= 0
    elif 7 <= slider1.get() <= 9:
        health_Head += 2
        health_Body += 1
        health_Legs += 1
    elif 9 < slider1.get() <= 12:
        health_Head += 1
        health_Body += 1
        health_Legs += 0

    #workout
    if slider2.get() ==0:
        health_Head -= 1
        health_Body -= 2
        health_Legs -= 2
    elif  slider2.get() <=1:
        health_Head += 0
        health_Body += 1
        health_Legs += 0
    elif slider2.get() <= 6:
        health_Head += 1
        health_Body += 2
        health_Legs += 1
    elif slider2.get() <= 12:
        health_Head += 1
        health_Body += 1
        health_Legs += 1

    #stress
    if 10 == slider3.get() or slider3.get() >=7:
        health_Head -= 3
        health_Body -= 2
        health_Legs -= 2
    elif 0 == slider3.get() or slider3.get() <=2:
        health_Head += 1
    elif 2== slider3.get() or slider3.get() <=6:
        health_Head -= 1
        health_Body -= 1
        health_Legs -= 1

    #vide
    if 7<=slider4.get() and slider4.get() <=10:
        health_Head += 2
        health_Body += 1
        health_Legs += 1
    elif 0== slider4.get() or slider4.get() <=2:
        health_Head -= 2
        health_Body -= 1
        health_Legs -= 1
    elif 2== slider4.get() or slider4.get() <=6:
        health_Head += 1
        health_Body += 0
        health_Legs += 0

    #screen time
    if slider5.get()<=2:
        pass
    elif  2<slider5.get() and slider5.get() <=7:
        health_Head -= 1
    elif 7< slider5.get() and slider5.get() >=15:
        health_Head -= 2
    
    #mob
    if mobings==1:
        health_Head -= 0
        health_Body -= 0
        health_Legs -= 0


# Functions that move from one canvas to another
def go_to_info():
    a.pack_forget()
    infocanva.pack()
def go_to_home():
    a.pack()
    infocanva.pack_forget()
def go_to_game():
    score()
    print(health_Head,health_Body,health_Legs)
    if health_Head >= 2:
        head = gamecanva.create_image(400,75,image=img_head_green)
    elif health_Head <= -2:
        head = gamecanva.create_image(400,75,image=img_head_red)
    elif health_Head <= 1:
        head = gamecanva.create_image(400,75,image=img_head_yellow)
    else:
        head = gamecanva.create_image(400,75,image=img_head)

    if health_Body >= 2:
        body = gamecanva.create_image(400,182,image=img_body_green)
    elif health_Body <= -2:
        body = gamecanva.create_image(400,182,image=img_body_red)
    elif health_Body <= -1:
        body = gamecanva.create_image(400,182,image=img_body_yellow)
    else:
        body = gamecanva.create_image(400,182,image=img_body)

    if health_Legs >= 2:
        legs = gamecanva.create_image(400,344,image=img_legs_green)
    elif health_Legs <= -2:
        legs = gamecanva.create_image(400,344,image=img_legs_red)
    elif health_Legs <= -1:
        legs = gamecanva.create_image(400,344,image=img_legs_yellow)
    else:
        legs = gamecanva.create_image(400,344,image=img_legs)

    gamecanva.pack()
    a.pack_forget()
def go_to_home_from_game():
     gamecanva.pack_forget()
     a.pack()

 

# functions that show the slider for gym and the othe yes or no

def yes_m():
    global mobings
    mobings = 1
def no_m():
    global mobings
    mobings = 0




# the functions that are the ones that show the results
def sleep():
    red1 = "Tu guli pārāk maz katru nakti, tev būtu jāguļ 7-9 stundas. Pārliecinieties, vai dienas laikā iegūstat pietiekami daudz saules gaismas, nedzer dzērienus, kuros ir kofeīnu, pārāk tuvu gulētiešanas laikam. Ekrāna laika ierobežošana pirms miega var arī palīdzēt samazināt miega problēmas."
    yellow1 = "Tu guli pārāk daudz tev būtu jāguļ 7-9 stundas. Tas var šķist vienkārši, bet viens, ko var darīt, ir ievērot noteiktu gulēšanas laiku un pamošanās laiku sev. Tas var palīdzēt ķermenim izveidot savu rutīnu, tādējādi palīdzot izvairīties no pārāk liela vai pārāk maza miega. Ja vēlies labāk izgulēties, būtiski ir pārliecināties, vai istabā ir tumšs. Lai ir klusums un arī telpas temperatūra ir jums patīkama. Ja ir par karstu vai par aukstu, tad izredzes, ka īpaši labi neizgulēsies."
    green1 = "Tu guli pietiekami daudz un nekas nav jāmaina. Tā turpini!"
    block = gamecanva.create_rectangle(550, 50, 750, 450, fill="white")
    if slider1.get() <= 2:
        sleep_tx = gamecanva.create_text(650, 250, text=red1, width=200, fill="black", font=("helvetica", 15))
    elif slider1.get() <= 4:
        sleep_tx = gamecanva.create_text(650, 250, text=red1, width=200, fill="black", font=("helvetica", 15))
    elif slider1.get() <= 6:
        sleep_tx = gamecanva.create_text(650, 250, text=red1, width=200, fill="black", font=("helvetica", 15))
    elif 7 <= slider1.get() <= 9:
        sleep_tx = gamecanva.create_text(650, 250, text=green1, width=200, fill="black", font=("helvetica", 15))
    elif 9 < slider1.get() <= 12:
        sleep_tx = gamecanva.create_text(650, 250, text=green1, width=200, fill="black", font=("helvetica", 12))

def gym():
    red2="Tu vingro par maz. Tev dienā vajag vingrot vismaz 30 minūtes. Vingrot var arī mājās bez speciāla inventāra."
    green2="Tu vingro pietiekami daudz! Tā turpini!"
    yellow2="Tu vingro ļoti daudz, esi uzmanīgs, lai nepārslogotu sevi."
    block = gamecanva.create_rectangle(550, 50, 750, 450, fill="white")
    if slider2.get() ==0:
        gym_tx = gamecanva.create_text(650, 250, text=red2, width=200, fill="black", font=("helvetica", 15))
    elif  slider2.get() <=2:
        gym_tx = gamecanva.create_text(650, 250, text=green2, width=200, fill="black", font=("helvetica", 15))
    elif 2< slider2.get() <= 6:
        gym_tx = gamecanva.create_text(650, 250, text=green2, width=200, fill="black", font=("helvetica", 15))
    elif 6< slider2.get() <= 12:
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
    elif 7< slider5.get() and slider5.get() <=15:
        screen_time_tx = gamecanva.create_text(650, 250, text=red5, width=200, fill="black", font=("helvetica", 15))
def mobings_j():
    green6="Tas labi ka pret tevi neviens nedara mobingu!"
    red6="Ja pats nevari tikt galā ar mobingu, tad lūdzu palīdzību draugiem, vecākiem un skolotājiem!"
    block = gamecanva.create_rectangle(550, 50, 750, 450, fill="white")
    if mobings==0:
        mobings_tx = gamecanva.create_text(650, 250, text=green6, width=200, fill="black", font=("helvetica", 15))
    else:
        mobings_tx = gamecanva.create_text(650, 250, text=red6, width=200, fill="black", font=("helvetica", 15))
style = {"troughcolor": "#505050", "sliderlength": 30, "sliderrelief": "flat", "background": "#4169E1"}



#  sliders

slider1 = Scale(root, from_=0, to=12, orient=HORIZONTAL, length=200, **style)
slider1.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
slider1.place(x=100, y=100)
a.create_window(125, 175, window=slider1)
slider1.config(showvalue=True, sliderlength=20,)

slider2 = Scale(root, from_=0, to=12, orient=HORIZONTAL, length=200, **style)
slider2.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
slider2.place(x=100, y=100)
slidder2_s=a.create_window(125, 265, window=slider2)
slider2.config(showvalue=True, sliderlength=20,)

slider3 = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=200, **style)
slider3.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
slider3.place(x=100, y=100)
a.create_window(125, 355, window=slider3)
slider3.config(showvalue=True, sliderlength=20,)

slider4 = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=200, **style)
slider4.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
slider4.place(x=100, y=100)
a.create_window(125, 445, window=slider4)
slider4.config(showvalue=True, sliderlength=20,)

slider5 = Scale(root, from_=0, to=15, orient=HORIZONTAL, length=200, **style)
slider5.config(troughcolor='#505050', sliderrelief='flat', highlightthickness=0)
slider5.place(x=100, y=100)
a.create_window(125, 550, window=slider5)
slider5.config(showvalue=True, sliderlength=20,)




# Buttons that move from one canvas to another canvas
a.tag_bind(info_bt,"<Button-1>", lambda event: go_to_info())
infocanva.tag_bind(go_back,"<Button-1>", lambda event: go_to_home())
a.tag_bind(game_bt,"<Button-1>",lambda event: go_to_game())
gamecanva.tag_bind(go_back_home,"<Button-1>",lambda event: go_to_home_from_game())

a.tag_bind(Apgalvojums6_ja,"<Button-1>",lambda event: yes_m())
a.tag_bind(Apgalvojums6_ne,"<Button-1>",lambda event: no_m())

# Buttons that show the results
gamecanva.tag_bind(sleep1,"<Button-1>",lambda event: sleep())
gamecanva.tag_bind(gym1,"<Button-1>",lambda event: gym())
gamecanva.tag_bind(stress1,"<Button-1>",lambda event: stress())
gamecanva.tag_bind(vide1,"<Button-1>",lambda event: vide())
gamecanva.tag_bind(screen_time1,"<Button-1>",lambda event: screen_time() )
gamecanva.tag_bind(mobings1,"<Button-1>",lambda event: mobings_j())


root.configure()
root.mainloop()