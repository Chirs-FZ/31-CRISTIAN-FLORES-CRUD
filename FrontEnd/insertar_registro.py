from tkinter import *
from tkinter import ttk
import prueba_database

window = Tk()
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

nombre = StringVar()
direccion = StringVar()
tarjeta = StringVar()

def crear_sala():

    nombre = entry_nombre.get()
    edad = entry_direccion.get()
    genero = entry_tarjeta.get()
  
    prueba_db = prueba_database.MyDatabase()
    pruena_db.insert_db(nombre, direccion, tarjeta)

frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=120)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)

title = Label(frame_navbar, 
              text="RESTAURANTE JAKE",
              font=("Century Gothic", "14"))
title.place(x=250, y=40)

title1 = Label(frame_title, 
              text="ORDENE SU PEDIDO", 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="Todos los campos son obligartorios.", 
              font=("Century Gothic", "14"),
              justify=LEFT)
title2.place(x=25, y=50)

frame_form = Frame(frame_options, width=350, height=450, bg="#d48df0")
frame_form.place(x=25, y=5)
label_sala = Label(frame_form, 
              text="Nombre:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_nombre.place(x=30, y=30)
entry_nombre = Entry(frame_form, justify=LEFT, width=25, 
             font=("Century Gothic", "14"))
entry_nombre.place(x=30, y=70)

label_direccion = Label(frame_form, 
              text="Direccion:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_direccion.place(x=30, y=100)
entry_direccion = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_direccion.place(x=30, y=140)

label_tarjeta = Label(frame_form, 
              text="Tarjeta:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_tarjeta.place(x=30, y=170)
entry_tarjeta = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_tarjeta.place(x=30, y=210)


button_agregar = Button(frame_form, text="Insertar almuerzo", 
                        font=("Century Gothic", "14", "bold"),
                        command=crear_sala)
button_agregar.place(x=110, y=350)

window.mainloop()
