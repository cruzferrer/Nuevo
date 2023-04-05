import tkinter as tk
class Inicio:
  def mostras():



    ventana = tk.Tk()
    ventana.title("Seleccionar tipo de usuario")
    ventana.configure(background="blue")
    ventana.geometry("300x300")

    hello = tk.Label(text="Producto")
    hello.pack()
    
    c = tk.Entry(ventana)
    c.pack()
    p = tk.Entry(ventana)
    p.pack()
    pv = tk.Entry(ventana)
    pv.pack()
    
    hello2 = tk.Label(text="Stock")
    hello2.pack()
    c2 = tk.Entry(ventana)
    c2.pack()
    can = tk.Entry(ventana)
    can.pack()

    no = tk.Label(text="Vender")
    no.pack()
    def Vender():
        from Vender import Vender
        Vender.Vender()
      
        
        

    
    boton = tk.Button(ventana, text="Maestro", command=Vender)
    
    
    con = tk.Entry(ventana)
    con.pack()


    

    file=open("Productos.txt", "w")
    file2=open("Stock.txt", "w")
    file3=open("Factura.txt", "w")
    
    file.write("Codigo: " + c + "\n")
    file.write("Producto: " + p + "\n")
    file.write("Pvp: " + pv + "\n")
    file.close()

    file2.write("Codigo: " + tex + "\n")
    file2.write("Cantidad: " + tex2 + "\n")
    file2.close()

    file3.write("Numero: " + tex + "\n")
    file3.write("Vendido: " + tex2 + "\n")
    file3.close()








    
    def seleccionar_maestro():
        print("Maestro seleccionado")
    
    def seleccionar_alumno():
        print("Alumno seleccionado")
    
    boton_maestro = tk.Button(ventana, text="Maestro", command=seleccionar_maestro)
    boton_alumno = tk.Button(ventana, text="Alumno", command=seleccionar_alumno)
    
    boton_maestro.pack(pady=20)
    boton_alumno.pack()
    
    ventana.mainloop()