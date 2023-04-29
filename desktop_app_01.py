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
ventana_principal.config(bg="gray")

#-----------------------------
# Frame entrada datos
#-----------------------------


frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white" , width=480 , height=180)
frame_entrada.place(x=10 , y=10)


#-----------------------------
# Frame operaciones
#-----------------------------


frame_operacipnes = Frame(ventana_principal)
frame_operacipnes.config(bg="white" , width=480 , height=100)
frame_operacipnes.place(x=10 , y=200)

#-----------------------------
# Frame operaciones
#-----------------------------


frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white" , width=480 , height=180)
frame_resultados.place(x=10 , y=310)
# run
# se ejecuta la funcion (metodos) mainloop() de la clase Tk() , atraves de la instancia ventana_principal. Este metodo despliega una
# ventana simple en la pantalla y queda a la espera de lo que el usuario haga . Cada accion del usuario se conoce como evento. El mainloop() es un bucle infinito

ventana_principal.mainloop()