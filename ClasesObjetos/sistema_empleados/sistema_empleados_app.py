from sistema_empleados.empleado import Empleado
from sistema_empleados.empresa import Empresa

print('*** Sistema de Empleados ***')

# Crear una instancia de una empresa
empresa1 = Empresa('Capcom')

# Contratar algunos empleados
empresa1.contratar_empleados('Matias', 'Desarrollo')
empresa1.contratar_empleados('Brisa', 'Marketing')
empresa1.contratar_empleados('Santiago', 'Ventas')
empresa1.contratar_empleados('Fabrizio', 'Ventas')

# Obtener el total de objetos de tipo empleado
print(f'Total de empleados: {Empleado.obtener_total_empleados()}')

# Obtener el numero de empleados en el departamento de ventas
print(f'Empleados en ventas: '
      f'{empresa1.obtener_numero_empleado_departamento('Ventas')}')

# Mostrar todos los empleados de la empresa
empresa1.obtener_total_empleados()
