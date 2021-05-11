from tkinter import *
from tkinter import messagebox
import sqlite3

# ---------------------------Funciones------------------------------------
def conexionBD():
    mi_conexion = sqlite3.connect("Usuarios")
    mi_cursor = mi_conexion.cursor()
    try:
        mi_cursor.execute('''
            CREATE TABLE DATOS_USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))         
            ''')
        messagebox.showinfo("BBDD","BBDD creada con exito")
    except:
        messagebox.showwarning("Atencion","La BBDD ya existe")

def salir_aplicacion():
    valor = messagebox.askquestion("Salir","Deseas salir de la palicación")
    if valor == "yes":
        root.destroy()

def limpiar_campos():
    mi_id.set("")
    mi_nombre.set("")
    mi_apellido.set("")
    mi_pass.set("")
    mi_direccion.set("")
    texto_comentario.delete(1.0,END)

def crear():
    mi_conexion = sqlite3.connect("Usuarios")
    mi_cursor = mi_conexion.cursor()
    mi_cursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,'" + mi_nombre.get() +
                      "','" + mi_apellido.get() +
                      "','" + mi_pass.get() +
                      "','" + mi_direccion.get() +
                      "','" + texto_comentario.get("1.0",END)+"')")

    mi_conexion.commit()
    messagebox.showinfo("BBDD","Registro insertado con exito")

def leer():
    mi_conexion = sqlite3.connect("Usuarios")
    mi_cursor = mi_conexion.cursor()
    mi_cursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID ="+ mi_id.get())
    el_usuario = mi_cursor.fetchall()
    for usuario in el_usuario:
        mi_id.set(usuario[0])
        mi_nombre.set(usuario[1])
        mi_apellido.set(usuario[2])
        mi_pass.set(usuario[3])
        mi_direccion.set(usuario[4])
        texto_comentario.insert(1.0,usuario[5])
    mi_conexion.commit()

def actualizar():
    mi_conexion = sqlite3.connect("Usuarios")
    mi_cursor = mi_conexion.cursor()
    mi_cursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO= '"+ mi_nombre.get()+
                      "',APELLIDO='"+mi_apellido.get()+
                      "',PASSWORD='"+mi_pass.get()+
                      "',DIRECCION='"+mi_direccion.get()+
                      "',COMENTARIOS='"+texto_comentario.get("1.0",END)+
                      "'WHERE ID =" + mi_id.get())

    mi_conexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado  con exito")

root = Tk()

#----------Creacion de la barra menu ---------------------
barra_menu = Menu(root)
root.config(menu = barra_menu, width= 300, height= 300)

bd_menu = Menu(barra_menu,tearoff =0)
bd_menu.add_command(label="Conectar", command = conexionBD)
bd_menu.add_command(label="Salir",command = salir_aplicacion)

borrar_menu = Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar campos",command = limpiar_campos)

crud_menu = Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear", command = crear)
crud_menu.add_command(label="Leer", command = leer)
crud_menu.add_command(label="Actualizar",command = actualizar)
crud_menu.add_command(label="Borrar")

ayuda_menu = Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Licencia")
ayuda_menu.add_command(label="Acerca de ...")

#COLOCAR LOS TITULOS A CADA ELEMENTO DE LA BARRA MENU
barra_menu.add_cascade(label = "BBDD", menu = bd_menu)
barra_menu.add_cascade(label = "Borrar", menu = borrar_menu)
barra_menu.add_cascade(label = "CRUD", menu = crud_menu)
barra_menu.add_cascade(label = "Ayuda", menu = ayuda_menu)

#--------------------Comienzo de campos ---------------------
mi_frame = Frame(root)
mi_frame.pack()

mi_id = StringVar()
mi_nombre = StringVar()
mi_apellido = StringVar()
mi_pass = StringVar()
mi_direccion = StringVar()

cuadro_ID = Entry(mi_frame, textvariable =mi_id)
cuadro_ID.grid(row =0, column = 1, padx =10,pady =10)

cuadro_nombre = Entry(mi_frame, textvariable =mi_nombre )
cuadro_nombre.grid(row =1, column = 1, padx =10,pady =10)
cuadro_nombre.config(fg= "red", justify = "right")

cuadro_apellido = Entry(mi_frame, textvariable = mi_apellido)
cuadro_apellido.grid(row =2, column = 1, padx =10,pady =10)
cuadro_apellido.config(fg= "red", justify = "right")

cuadro_pass = Entry(mi_frame, textvariable = mi_pass)
cuadro_pass.grid(row =3, column = 1, padx =10,pady =10)
cuadro_pass.config(show = "*")

cuadro_direccion = Entry(mi_frame, textvariable =mi_direccion)
cuadro_direccion.grid(row =4, column = 1, padx =10,pady =10)

texto_comentario = Text(mi_frame, width = 16, height = 5)
texto_comentario.grid(row = 5, column = 1, padx = 10, pady = 10)
scroll_vertical = Scrollbar(mi_frame, command = texto_comentario.yview())
scroll_vertical.grid(row = 5, column = 2, sticky = "nsew")   #sticky para que se ajuste al area de texto
texto_comentario.config(yscrollcommand = scroll_vertical.set)

# ------------------ Aqui comienzan los label -----------------------------
id_label = Label(mi_frame, text="ID:")
id_label.grid(row=0, column = 0, sticky = "e",padx= 10, pady = 10)

nombre_label = Label(mi_frame, text="Nombre:")
nombre_label.grid(row=1, column = 0, sticky = "e",padx= 10, pady = 10)

apellido_label = Label(mi_frame, text="Apellido:")
apellido_label.grid(row=2, column = 0, sticky = "e",padx= 10, pady = 10)

pass_label = Label(mi_frame, text="Password:")
pass_label.grid(row=3, column = 0, sticky = "e",padx= 10, pady = 10)

direccion_label = Label(mi_frame, text="Direccion:")
direccion_label.grid(row=4, column = 0, sticky = "e",padx= 10, pady = 10)

comentarios_label = Label(mi_frame, text="Comentarios:")
comentarios_label.grid(row=5, column = 0, sticky = "e",padx= 10, pady = 10)

#---------------------- Aqui van los botones ------------------
mi_frame_2 = Frame(root)
mi_frame_2.pack()

boton_crear = Button(mi_frame_2, text = "Create",command = crear)
boton_crear.grid(row=0,column = 0, sticky = "e", padx = 10, pady = 10)

boton_leer = Button(mi_frame_2, text = "Read", command = leer)
boton_leer.grid(row=0,column = 1, sticky = "e", padx = 10, pady = 10)

boton_actualizar = Button(mi_frame_2, text = "Update", command = actualizar)
boton_actualizar.grid(row=0,column = 2, sticky = "e", padx = 10, pady = 10)

boton_borrar = Button(mi_frame_2, text = "Delete")
boton_borrar.grid(row=0,column = 3, sticky = "e", padx = 10, pady = 10)


root.mainloop()