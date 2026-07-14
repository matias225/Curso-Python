print('*** break y continue *** ')

# Ejemplo con break
print('break:')
for numero in range(1, 10):
    if numero % 2 == 0: # Número par
        print(numero)
        break # Salimos del ciclo inmediatamente

# Ejemplo con continue
print('\ncontinue:')
for numero in range(1, 10):
    if numero % 2 == 1: # Número impar
        continue
    print(numero) # Sólo números pares
