
import tkinter as tk

window = tk.Tk()
window.title("INICIO DE SESION")
window.geometry("300x300")

hello = tk.Label(text="Usuario")
hello.pack()
usu = tk.Entry(window)
usu.pack()

hello2 = tk.Label(text="Contraseña")
hello2.pack()

con = tk.Entry(window)
con.pack()


def obtener():
  usuario = usu.get()
  contra = con.get()

  def cifrado_cesar(texto, desplazamiento):
    tex = ""
    for letra in texto:
      if letra.isupper():
        valor_ascii = ord(letra)
        nuevo_valor_ascii = (valor_ascii + desplazamiento - 65) % 26 + 65
        tex += chr(nuevo_valor_ascii)
      elif letra.islower():
        valor_ascii = ord(letra)
        nuevo_valor_ascii = (valor_ascii + desplazamiento - 97) % 26 + 97
        tex += chr(nuevo_valor_ascii)
      else:
        tex += letra
    return tex

  desplazamiento = 20
  tex = cifrado_cesar(usuario, desplazamiento)
  print(tex)
  tex2 = cifrado_cesar(contra, desplazamiento)
  print(tex2)

  archivo = open("datos.txt", "w")

  archivo.write("Usuario: " + tex + "\n")
  archivo.write("Contraseña: " + tex2 + "\n")
  archivo.close()


boton = tk.Button(window, text="Aceptar", command=obtener)
boton.pack()

Inicio = tk.Label(text="Inicio de sesion")
Inicio.pack()

h = tk.Label(text="Usuario")
h.pack()
u = tk.Entry(window)
u.pack()

h2 = tk.Label(text="Contraseña")
h2.pack()

c = tk.Entry(window)
c.pack()


def comenzar():
  us = u.get()
  cc = c.get()
  print(us)
  print(cc)

  archivo = open("datos.txt", "r")
  contenido = archivo.read().split()

  for i in range(len(contenido)):
    if contenido[i] == "Usuario:":
      usuario = contenido[i + 1]
      break

  for j in range(len(contenido)):
    if contenido[j] == "Contraseña:":
      contra = contenido[j + 1]
      break

  #cifrado inverso, la quiero mucho profa

  def cifrado_inverso(mensaje, desplazamiento):
    mensaje_cifrado = ""
    desplazamiento = -desplazamiento
    for letra in mensaje:
      if letra.isalpha():

        codigo_ascii = ord(letra)

        codigo_ascii += desplazamiento

        if letra.isupper():
          if codigo_ascii < 65:
            codigo_ascii += 26
          elif codigo_ascii > 90:
            codigo_ascii -= 26
        elif letra.islower():
          if codigo_ascii < 97:
            codigo_ascii += 26
          elif codigo_ascii > 122:
            codigo_ascii -= 26

        letra_cifrada = chr(codigo_ascii)
        mensaje_cifrado += letra_cifrada
      else:

        mensaje_cifrado += letra
    return mensaje_cifrado

  desplazamiento = 20
  desifrado = cifrado_inverso(usuario, desplazamiento)
  print(desifrado)
  desifrado2 = cifrado_inverso(contra, desplazamiento)
  print(desifrado2)

  if us == desifrado:
    window.destroy()
    from inicio import Inicio
    Inicio.mostras()


boton2 = tk.Button(window, text="Aceptar", command=comenzar)
boton2.pack()

tk.mainloop()
