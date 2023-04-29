# se importa la libreria tkinter con todas sus funciones

from tkinter import *

#--------------------------
# Funciones de la app
#--------------------------

#--------------------------
# Ventana principal
#--------------------------


# se declara una variable llamada ventana_principal , que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk() 

# titulo de la ventana
ventana_principal.title("Sistemas UIS Socorro")

# tamaño de la ventana en pixeles
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)


# color de fondo de la ventana
ventana_principal.config(bg="white")

#-----------------------------
# Frame entrada datos
#-----------------------------


frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="red" , width=140 , height=200)
frame_entrada.place(x=0 , y=0)


#-----------------------------
# Frame operaciones
#-----------------------------


frame_operacipnes = Frame(ventana_principal)
frame_operacipnes.config(bg="blue" , width=500 , height=50)
frame_operacipnes.place(x=0 , y=230)

#-----------------------------
# Frame operaciones
#-----------------------------


frame_ops = Frame(ventana_principal)
frame_ops.config(bg="blue" , width=50 , height=500)
frame_ops.place(x=160 , y=0)

#-----------------------------
# Frame operaciones
#-----------------------------


frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="red" , width=140 , height=230)
frame_resultados.place(x=0 , y=320)


#-----------------------------
# Frame operaciones
#-----------------------------


frame_per = Frame(ventana_principal)
frame_per.config(bg="red" , width=300 , height=270)
frame_per.place(x=250 , y=320)


#-----------------------------
# Frame operaciones
#-----------------------------


frame_pera = Frame(ventana_principal)
frame_pera.config(bg="red" , width=200 , height=250)
frame_pera.place(x=2500 , y=0)

# run
# se ejecuta la funcion (metodos) mainloop() de la clase Tk() , atraves de la instancia ventana_principal. Este metodo despliega una
# ventana simple en la pantalla y queda a la espera de lo que el usuario haga . Cada accion del usuario se conoce como evento. El mainloop() es un bucle infinito

ventana_principal.mainloop()