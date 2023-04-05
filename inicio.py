import tkinter as tk
class Inicio:
  def mostras():


    
    ventana = tk.Tk()
    ventana.title("Producto")
    ventana.configure(background="blue")
    ventana.geometry("400x300")
  #AAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    hello = tk.Label(text="Producto")
    hello.pack()
    
    c = tk.Entry(ventana)
    c.pack()
    ca = c.get()
    
    p = tk.Entry(ventana)
    p.pack()
    pa = p.get()
    
    pv = tk.Entry(ventana)
    pv.pack()
    pva = pv.get()
  #BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
    hello2 = tk.Label(text="Stock")
    hello2.pack()
    c2 = tk.Entry(ventana)
    c2.pack()
    c2b= c2.get()
    
    can = tk.Entry(ventana)
    can.pack()
    cana = can.get()
    
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    

    
    def Vender():
        from Vender import Vender
        Vender.Vender()
      
        
        
    #OOOOOOOOOOORRFOOOO22OI2OOIOOLABELS
    
    LAB = tk.Label(text="Stock")
    LAB.pack()
    LAB.place(x=10, y=20)

    #00000000000000000000000990?///////
    
    boton = tk.Button(ventana, text="Vender", command=Vender)
    boton.pack()
    boton.place(x=160, y=200)
    
    


    

    file=open("Productos.txt", "w")
    file2=open("Stock.txt", "w")
    
    
    file.write("Codigo: " + ca + "\n")
    file.write("Producto: " + pa + "\n")
    file.write("Pvp: " + pva + "\n")
    file.close()

    file2.write("Codigo: " + c2b + "\n")
    file2.write("Cantidad: " + cana + "\n")
    file2.close()

    








    
    
    
   
    
    ventana.mainloop()