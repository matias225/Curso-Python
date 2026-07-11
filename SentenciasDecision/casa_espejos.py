print('*** Bienvenidos a La Casa de los Espejos ***')

edad = int(input("Ingrese su edad: "))
tiene_miedo_oscuridad = input("¿Tienes miedo a la oscuridad? (Si/No) ")
tiene_miedo_oscuridad = tiene_miedo_oscuridad.lower().strip() == 'si'

if not tiene_miedo_oscuridad and edad >= 10:
    print('Puedes entrar a La Casa de los Espejos')
else:
    print('Lo siento, La Casa de los Espejos podria darte miedo')