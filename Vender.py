import tkinter as tk
class Vender:
  def Vender():
    ventana = tk.Tk()
    ventana.title("Venta")
    ventana.configure(background="blue")
    ventana.geometry("400x300")
    
    no = tk.Label(text="Vender")
    no.pack()
    no.place(x=20, y=10)
    x = tk.Entry(ventana)
    x.pack()
    x.place(x=20, y=30)
    xa = x.get()
    
    ven = tk.Entry(ventana)
    ven.pack()
    ven.place(x=20, y=60)
    vena = ven.get()
    

    



    file3=open("Factura.txt", "w")
    file3.write("Numero: " + xa + "\n")
    file3.write("Vendido: " + vena + "\n")
    file3.close()


    def regresar():
      ventana.destroy()
      from inicio import Inicio
      Inicio.mostras()
      
    boton = tk.Button(ventana, text="Regresar", command=regresar)
    boton.pack()
    boton.place(x=160, y=200)


    
    ventana.mainloop()