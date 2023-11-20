from tkinter import *
#import os
from PIL import ImageTk, Image
import obtencion_datos as od
import comprobaciones as comp
import algoritmo_ids as alg

def on_button_click():
    # Obtener el valor del cuadro de texto
    texto_ingresado1 = cuadroTexto1.get()
    texto_ingresado2 = cuadroTexto2.get()

    try:
        # Intentar convertir el texto a un número entero
        numero_entero1 = int(texto_ingresado1)
        numero_entero2 = int(texto_ingresado2)
        
        result_path = alg.iterative_ids(G, numero_entero1, numero_entero2, initial_depth_limit, max_depth_limit)

        if result_path is not None:
            print("Camino encontrado:", result_path)
        else:
            print("No se encontró un camino dentro de los límites de profundidad especificados.")

        alg.draw_graph(G, result_path)
        alg.draw_subgraph(G, result_path)
        
    except ValueError:
        # Manejar el caso en el que no se pueda convertir a entero
        print("Error: El texto no es un número entero válido")

estado = comp.comprobacion()

if estado == 1:
    print("El grafo ya se ha generado previamente")
    texto = "Muestra: 1500 personas\n\nRango de amigos: de 7 a 9\n\n¿Grafo generado por \nprimera vez en \nel dispositivo?: NO"
    G = od.load_graph_from_txt("grafo.txt")
else:
    print("El grafo no se ha generado aun")
    input()
    print("Generando el grafo...")
    grafo = od.generarGrafo()
    print("¡Grafo generado!")
    G = od.load_graph_from_txt("grafo.txt")
    texto = "Muestra: 1500 personas\n\nRango de amigos: de 7 a 9\n\n¿Grafo generado por \nprimera vez en \nel dispositivo?: SÍ"
    input()
    
raiz = Tk()

raiz.title("Programa 'Conocidos Desconocidos'")
raiz.resizable(False, False)
raiz.iconbitmap("grafos_logo.ico")
raiz.geometry("800x600")
raiz.config(bg = "sky blue")

frame1 = Frame(raiz)

frame1.pack(side = "right", anchor = "s")
#frame1.pack(fill="both", expand="True")
frame1.config(bg = "white")
frame1.config(width = "500", height = "400")
frame1.config(bd =  5)  
frame1.config(relief = "ridge")
frame1.config(cursor="hand2")
#frame1.place(x = 150, y = 100)

label1 = Label(raiz, text = "Conocidos Desconocidos", fg = "black", font = ("Comic Sans MS", 20), bg = "sky blue")
label1.place(x = 20, y = 15)
imagen = ImageTk.PhotoImage(Image.open("grafo.png").resize((500,400)))
Label(frame1, image = imagen).place(x = 0, y = 0)

Label(raiz, text = "Ingrese el código de la primera persona", fg = "black", font = ("Comic Sans MS", 12), bg = "sky blue").place(x = 20, y = 100)

cuadroTexto1 = Entry(raiz, width=20)
cuadroTexto1.place(x=20, y=140)

Label(raiz, text = "Ingrese el código de la segunda persona", fg = "black", font = ("Comic Sans MS", 12), bg = "sky blue").place(x = 400, y = 100)

cuadroTexto2 = Entry(raiz, width=20)
cuadroTexto2.place(x=400, y=140)


Label(raiz, text = texto, fg = "black", font = ("Comic Sans MS", 14), bg = "sky blue", justify="left").place(x = 20, y = 330)

Label(raiz, text = "Encontrar una conexión\nentre ambas personas", fg = "black", font = ("Comic Sans MS", 12), bg = "sky blue", justify="left").place(x = 20, y = 180)

boton = Button(raiz, text = "¡Haga click aquí!", font = ("Comic Sans MS", 10), command=on_button_click)
boton.place(x = 20, y = 240)


initial_depth_limit = 2
max_depth_limit = 5


raiz.mainloop() 
