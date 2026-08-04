import tkinter as tk
# Mejora de los componentes
from tkinter import ttk

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.configure(bg='#1d2d44')

# Creamos una etiqueta (label)
etiqueta = ttk.Label(ventana, text='Saludos')

# Cambiar el texto usando el metodo configure
etiqueta.configure(text='Nos vemos...')

# Cambiar el texto con ayuda de la llave text
etiqueta['text'] = 'La proxima'

# Publicamos el componente
etiqueta.pack(pady=20)

ventana.mainloop()
