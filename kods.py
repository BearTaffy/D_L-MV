from tkinter import*
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
root.mainloop()