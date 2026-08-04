import tkinter as tk
# Mejora de los componentes
from tkinter import ttk

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.configure(bg='#1d2d44')

def saludar(nombre):
    print(f'Saludos {nombre}, desde el boton')

boton1 = ttk.Button(ventana, text='Enviar', command=lambda: saludar('Brisa'))
boton1.pack(pady=20)

ventana.mainloop()
