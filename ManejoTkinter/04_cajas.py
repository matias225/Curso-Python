import tkinter as tk
# Mejora de los componentes
from tkinter import ttk

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.configure(bg='#1d2d44')

def mostrar():
    texto = caja_texto.get() # Recuperamos el valor de la caja de texto
    print(f'Texto proporcionado: {texto}')
    etiqueta.config(text=texto)

# Caja de texto
caja_texto = ttk.Entry(ventana, font=('Arial', 15))
caja_texto.pack(pady=20)

# Agregamos un boton
boton1 = ttk.Button(ventana, text='Enviar', command=mostrar)
boton1.pack(pady=20)

# Agregamos una etiqueta
etiqueta = ttk.Label(ventana, text='Valor inicial')
etiqueta.pack(pady=20)

ventana.mainloop()
