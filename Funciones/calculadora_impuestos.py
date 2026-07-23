print('*** Calculadora de impuestos ***')

def calcular_pago_total(monto_sin_impuesto, impuesto_a_aplicar):
    return monto_sin_impuesto + monto_sin_impuesto * (impuesto_a_aplicar/100)

if __name__ == '__main__':
    monto = float(input('Ingresa el pago sin impuesto: '))
    impuesto = float(input('Ingresa el impuesto: '))
    monto_total = calcular_pago_total(monto, impuesto)
    print(f'El monto total con impuestos es de: ${monto_total}')
