import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from zona_fit_gui.cliente import Cliente
from zona_fit_gui.cliente_dao import ClienteDAO

class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.id_cliente = None
        self.frame_botones = None
        self.membresia_entry = None
        self.apellido_entry = None
        self.nombre_entry = None
        self.frame_form = None
        self.tabla = None
        self.frame_tabla = None
        self.estilos = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=self.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')
        self.estilos.configure(self, background=self.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black',)

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 20),
                             background=self.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_form = ttk.Frame()
        # Nombre
        nombre_lbl = ttk.Label(self.frame_form, text='Nombre: ')
        nombre_lbl.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_entry = ttk.Entry(self.frame_form)
        self.nombre_entry.grid(row=0, column=1)
        # Apellido
        apellido_lbl = ttk.Label(self.frame_form, text='Apellido: ')
        apellido_lbl.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_entry = ttk.Entry(self.frame_form)
        self.apellido_entry.grid(row=1, column=1)
        # Membresia
        membresia_lbl = ttk.Label(self.frame_form, text='Membresia: ')
        membresia_lbl.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_entry = ttk.Entry(self.frame_form)
        self.membresia_entry.grid(row=2, column=1)

        # Publicar el frame de form
        self.frame_form.grid(row=1, column=0)

    def cargar_tabla(self):
        # Creamos un frame para mostrar la tabla
        self.frame_tabla = tk.Frame(self)
        self.estilos.configure('Treeview', background='black',
                               foreground='white',
                               fieldbackground='black',
                               rowheight=20)
        # Definimos las columnas
        columnas = ('Id','Nombre','Apellido','Membresia')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # Agregar las cabeceras
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresia', anchor=tk.W)

        # Definir las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)

        # Cargar los datos desde la db
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre,
                                      cliente.apellido, cliente.membresia))

        # Agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Asociar el evento select
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0)
        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()
        # Crear los botones
        # Botón agregar
        agregar_boton = ttk.Button(self.frame_botones, text='Guardar',
                                   command=self.validar_cliente)
        agregar_boton.grid(row=0, column=0, padx=30)
        # Botón agregar
        eliminar_boton = ttk.Button(self.frame_botones, text='Eliminar',
                                   command=self.eliminar_cliente)
        eliminar_boton.grid(row=0, column=1, padx=30)
        # Botón limpiar
        limpiar_boton = ttk.Button(self.frame_botones, text='Limpiar',
                                    command=self.limpiar_formulario)
        limpiar_boton.grid(row=0, column=2, padx=30)

        # Aplicar un estilo a los botones
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        # Publicar el frame de botones
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

    def validar_cliente(self):
        # Validar los campos
        if self.nombre_entry.get() and self.apellido_entry.get() and self.membresia_entry.get():
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atencion', message='El valor de membresia NO es numerico')
                self.membresia_entry.delete(0, tk.END)
                self.membresia_entry.focus_set()
        else:
            showerror(title='Atencion', message='Debe llenar el formulario')
            self.nombre_entry.focus_set()

    def validar_membresia(self):
        try:
            int(self.membresia_entry.get())
            return True
        except:
            return False

    def guardar_cliente(self):
        # Recuperar los valores de las cajas de texto
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        membresia = self.membresia_entry.get()
        # Validamos el valor del self.id_cliente
        if self.id_cliente is None:
            cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDAO.insertar(cliente)
            showinfo(title='Agregado', message='Cliente agregado correctamente...')
        else: # Actualizar
            cliente = Cliente(self.id_cliente, nombre, apellido, membresia)
            ClienteDAO.actualizar(cliente)
            showinfo(title='Actualizado', message='Cliente actualizado...')
        # Volvemos a mostrar los datos y limpiamos el formulario
        self.recargar_datos()

    def cargar_cliente(self, event):
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_texto = elemento['values'] # tupla de valores del cliente seleccionado
        # Recuperar cada valor del cliente
        self.id_cliente = cliente_texto[0]
        nombre = cliente_texto[1]
        apellido = cliente_texto[2]
        membresia = cliente_texto[3]
        # Antes de cargar, limpiamos el formulario
        self.limpiar_formulario()
        # Cargar los valores en el formulario
        self.nombre_entry.insert(0, nombre)
        self.apellido_entry.insert(0, apellido)
        self.membresia_entry.insert(0, membresia)

    def recargar_datos(self):
        # Volver a cargar los datos de la tabla
        self.cargar_tabla()
        # Limpiar los datos
        self.limpiar_datos()

    def eliminar_cliente(self):
        if self.id_cliente is None:
            showerror(title='Atencion', message='Debe seleccionar un cliente a eliminar')
        else:
            cliente = Cliente(self.id_cliente)
            ClienteDAO.eliminar(cliente)
            showinfo(title='Eliminado', message='Cliente eliminado...')
            self.recargar_datos()

    def limpiar_datos(self):
        self.limpiar_formulario()
        self.id_cliente = None

    def limpiar_formulario(self):
        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)
        self.membresia_entry.delete(0, tk.END)

if __name__ == '__main__':
    app = App()
    app.mainloop()
