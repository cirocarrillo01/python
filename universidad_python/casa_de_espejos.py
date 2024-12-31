#--------- casa de espejos ------------
print('--- bienvenidos a la casa de los espejos ---')

edad = int(input('Cual es tu edad?: '))
tienes_miedo_oscuridad = input('Tienes miedo a la oscuridad (SI/NO)?: ')
tienes_miedo_oscuridad = tienes_miedo_oscuridad.strip().lower() == 'si'

if not tienes_miedo_oscuridad and edad >= 10:
    print('puedes entrar a la casa de los espejos')
else:
    print('lo siento, la casa de los espejos prodria darte miedo')









