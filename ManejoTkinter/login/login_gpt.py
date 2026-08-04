import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Función para validar el login
# -----------------------------
def validar_login():
    usuario = entry_usuario.get().strip()
    password = entry_password.get().strip()

    if usuario == "root" and password == "admin":
        messagebox.showinfo("Login", "Valores correctos")
    else:
        messagebox.showerror("Login", "Valores incorrectos")


# -----------------------------
# Ventana principal
# -----------------------------
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("420x260")
ventana.configure(bg="#121212")
ventana.resizable(False, False)

# -----------------------------
# Frame principal
# -----------------------------
frame = tk.Frame(
    ventana,
    bg="#1E1E1E",
    padx=20,
    pady=20,
    highlightbackground="#3A3A3A",
    highlightthickness=1
)
frame.place(relx=0.5, rely=0.5, anchor="center")

# -----------------------------
# Título
# -----------------------------
lbl_titulo = tk.Label(
    frame,
    text="Login",
    font=("Segoe UI", 18, "bold"),
    bg="#1E1E1E",
    fg="white"
)
lbl_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# -----------------------------
# Usuario
# -----------------------------
lbl_usuario = tk.Label(
    frame,
    text="Usuario:",
    font=("Segoe UI", 11),
    bg="#1E1E1E",
    fg="white"
)
lbl_usuario.grid(row=1, column=0, sticky="e", padx=10, pady=8)

entry_usuario = tk.Entry(
    frame,
    width=22,
    font=("Segoe UI", 11),
    bg="#2B2B2B",
    fg="white",
    insertbackground="white",
    relief="flat"
)
entry_usuario.grid(row=1, column=1, padx=10, pady=8)

# -----------------------------
# Contraseña
# -----------------------------
lbl_password = tk.Label(
    frame,
    text="Contraseña:",
    font=("Segoe UI", 11),
    bg="#1E1E1E",
    fg="white"
)
lbl_password.grid(row=2, column=0, sticky="e", padx=10, pady=8)

entry_password = tk.Entry(
    frame,
    width=22,
    font=("Segoe UI", 11),
    bg="#2B2B2B",
    fg="white",
    insertbackground="white",
    relief="flat",
    show="*"
)
entry_password.grid(row=2, column=1, padx=10, pady=8)

# -----------------------------
# Botón
# -----------------------------
btn_enviar = tk.Button(
    frame,
    text="Enviar",
    font=("Segoe UI", 11, "bold"),
    bg="#3A86FF",
    fg="white",
    activebackground="#2563EB",
    activeforeground="white",
    relief="flat",
    padx=10,
    command=validar_login
)
btn_enviar.grid(row=3, column=0, columnspan=2, pady=(20, 5), sticky="ew")

# Dar foco al usuario
entry_usuario.focus()

# Ejecutar aplicación
ventana.mainloop()
