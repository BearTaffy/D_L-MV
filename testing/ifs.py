from tkinter import*

root=Tk()
root.title("Mentālā veselība")
garums=800 #x
platums=500 #y
a=Canvas(root,width=garums,height=platums,bg="#4d4dff")
a.pack()

img_BG = PhotoImage(file="testing/man.png")
BG = a.create_image(garums/2,platums/2,image=img_BG)
a.create_text(650,480,text="Atpakaļ uz jautājumiem",fill="#660066",font=("Helvetica",20))



img_legs = PhotoImage(file="person/Legs/legs_yellow.png")
legs = a.create_image(400,344,image=img_legs)
img_head = PhotoImage(file="person/Head/head_red.png")
head = a.create_image(400,75,image=img_head)
img_body = PhotoImage(file="person/Body/body_green.png")
body = a.create_image(400,182,image=img_body)


if health_Head >= 3:
    img_head = PhotoImage(file="person/Head/head_green.png")
    head = gamecanva.create_image(400,75,image=img_head)
elif health_Head <= -3:
    img_head = PhotoImage(file="person/Head/head_yellow.png")
    head = gamecanva.create_image(400,75,image=img_head)
elif health_Head <= -1:
    img_head = PhotoImage(file="person/Head/head_Red.png")
    head = gamecanva.create_image(400,75,image=img_head)
else:
    img_head = PhotoImage(file="person/Head/head_normal.png")
    head = gamecanva.create_image(400,75,image=img_head)


if health_Body >= 3:
    img_body = PhotoImage(file="person/Body/body_green.png")
    body = gamecanva.create_image(400,75,image=img_body)
elif health_Body <= -3:
    img_body = PhotoImage(file="person/Body/body_yellow.png")
    body = gamecanva.create_image(400,75,image=img_body)
elif health_Body <= -1:
    img_body = PhotoImage(file="person/Body/body_Red.png")
    body = gamecanva.create_image(400,75,image=img_body)
else:
    img_body = PhotoImage(file="person/Body/body_normal.png")
    body = gamecanva.create_image(400,75,image=img_body)


if health_Legs >= 3:
    img_legs = PhotoImage(file="person/Head/head_green.png")
    legs = gamecanva.create_image(400,75,image=img_legs)
elif health_Legs <= -3:
    img_legs = PhotoImage(file="person/Head/head_yellow.png")
    legs = gamecanva.create_image(400,75,image=img_legs)
elif health_Legs <= -1:
    img_legs = PhotoImage(file="person/Head/head_Red.png")
    legs = gamecanva.create_image(400,75,image=img_legs)
else:
    img_legs = PhotoImage(file="person/Head/head_normal.png")
    legs = gamecanva.create_image(400,75,image=img_legs)

def callback(event):
    print( "clicked at", event.x, event.y)

a.bind("<Button-1>", callback)
root.mainloop()