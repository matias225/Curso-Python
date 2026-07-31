from zona_fit_db import cliente_dao
from zona_fit_db.cliente_dao import ClienteDAO
from zona_fit_db.cliente import Cliente

class AppZonaFit:
    cliente_dao = ClienteDAO()

    def app_zona_fit(self):
        salir = False
        while not salir:
            opcion = self.mostrar_menu()
            salir = self.ejecutar_opcion(opcion)

    def mostrar_menu(self):
        print('''
Menu
    1. Listar clientes
    2. Agregar cliente
    3. Modificar cliente
    4. Eliminar cliente
    5. Salir
''')
        return int(input('Seleccione una opcion (1-5): '))

    def ejecutar_opcion(self, opcion):
        if opcion == 1: # Listar clientes
            clientes = self.cliente_dao.seleccionar()
            print('\n--- Listado de clientes ---')
            for cliente in clientes:
                print(cliente)
            return None
        elif opcion == 2: # Agregar
            nombre = input('Ingrese el nombre del cliente: ')
            apellido = input('Ingrese el apellido del cliente: ')
            membresia = int(input('Ingrese la membresia del cliente: '))
            nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            clientes_agregados = self.cliente_dao.insertar(nuevo_cliente)
            print(f'Se agrego correctamente {clientes_agregados} cliente.')
            return None
        elif opcion == 3: # Modificar
            id_cliente = int(input('Ingrese el id del cliente a modificar: '))
            nombre = input('Ingrese el nombre modificado: ')
            apellido = input('Ingrese el apellido modificado: ')
            membresia = int(input('Ingrese el membresia modificado: '))
            cliente_actualizar = Cliente(id_cliente, nombre, apellido, membresia)
            clientes_actualizados = self.cliente_dao.actualizar(cliente_actualizar)
            if clientes_actualizados != 0:
                print(f'Se actualizo el cliente con el id: {id_cliente}')
            else:
                print(f'\nNo existe un cliente con el id: {id_cliente}')
            return None
        elif opcion == 4: # Eliminar
            id_eliminar = int(input('Ingrese el id del cliente a eliminar: '))
            cliente_eliminar = Cliente(id=id_eliminar)
            clientes_eliminados = self.cliente_dao.eliminar(cliente_eliminar)
            if clientes_eliminados != 0:
                print(f'\nSe elimino el cliente con el id: {id_eliminar}')
            else:
                print(f'\nNo existe un cliente con el id: {id_eliminar}')
            return None
        elif opcion == 5: # Salir
            print('\nSaliendo...')
            return True
        else:
            print('Opcion invalida.')
            return None

# Programa principal
if __name__ == '__main__':
    app = AppZonaFit()
    app.app_zona_fit()