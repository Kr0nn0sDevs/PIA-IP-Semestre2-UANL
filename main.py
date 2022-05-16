from grafica import *
from tkinter import *
from masinfo import *


raiz=Tk()
raiz.title("Pia de Introduccion a la Programacion")
raiz.config(bg="violet")
raiz.config(bd=25)
raiz.config(relief="ridge")

raiz.iconbitmap("imagen.ico")
lab=Label(raiz, text=" Web scraping  ", font=("Comic San MS", 30), bg="violet").place(x=530, y=0)
im=PhotoImage(file="lebron.png")

def codigo():
    Label(raiz,text=x, font=("Comic San MS", 10), bg="purple").place(x=30,y=200)

def codig():
    Label(raiz,text=inte, font=("Comic San MS", 10), bg="purple").place(x=500,y=200)

def cod():
    Label(raiz,text="Proximos Juegos", font=("Comic San MS", 10), bg="purple").place(x=900,y=200)

def co():
    Label(raiz, image=im).place(x=300, y=250)

def co2():
    Label(raiz, text=y2,font=("Comic San MS", 10), bg="purple").place(x=1000,y=500)

bot=Button(raiz, text="Informacion", bg="violet", command=codigo,font=("Comic San MS", 30)).place(x=100, y=100)
boot=Button(raiz, text="Integrantes", bg="violet", command=codig,font=("Comic San MS", 30)).place(x=500, y=100)

bo=Button(raiz, text="Proximos Juegos", bg="violet", command=cod,font=("Comic San MS", 30)).place(x=900, y=100)

bt=Button(raiz, text="Foto", bg="violet", command=co,font=("Comic San MS", 30)).place(x=100, y=400)
bt=Button(raiz, text="Noticias", bg="violet", command=co2,font=("Comic San MS", 30)).place(x=1000, y=400)

raiz.mainloop()
