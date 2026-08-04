import tkinter as tk

# Creamos una ventana
ventana = tk.Tk()

# Redimensionar la ventana
ventana.geometry('600x400')

# Modificar titulo
ventana.title('Nueva ventana')

# Evitar redimensionar la ventana
ventana.resizable(0, 0)

# Color de la ventana
ventana.configure(bg='#1d2d44')

# Hacemos visible la ventana
ventana.mainloop()
