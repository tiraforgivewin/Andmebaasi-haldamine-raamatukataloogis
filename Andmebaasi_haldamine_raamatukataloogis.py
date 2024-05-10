from tkinter import *
import sqlite3


aken=Tk()
aken.geometry("1500x1000")
aken.title("Tkineri kasutamine")

tekst1="Ruutvõrrandi lahendamine"
tekst2="Lahendus"
tekst3 = "Graafik"






pealkiri=Label(aken,
               text="db Raamatukogu",
               bg="#b4f596",
               fg="#000000",
               font="Arial 20",
               height=2,
               width=20)


AutoridForm=Label(aken, 
             text="Autorid",
             bg="#82b7e7",
             fg="#000000",
             font="Arial 20",
             height=2,
             width=10
             )
ŽanridForm=Label(aken, 
             text="Žanrid",
             bg="#82b7e7",
             fg="#000000",
             font="Arial 20",
             height=2,
             width=10
             )
RaamatudForm=Label(aken, 
             text="Raamatud",
             bg="#82b7e7",
             fg="#000000",
             font="Arial 20",
             height=2,
             width=10
             )


pealkiri.grid(row=0,column=6,columnspan=6)
AutoridForm.grid(row=1,column=1)
ŽanridForm.grid(row=1,column=2)
RaamatudForm.grid(row=1,column=3)
aken.mainloop()