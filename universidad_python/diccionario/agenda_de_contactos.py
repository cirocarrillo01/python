# ----- agenda de contactos ----------------------------
print('----- agenda de contactos ------')
agenda = {
    'carlos':{
        'telefono': '254136987',
        'email': 'sal@mail.com',
        'direccion': 'gfd-258'
    },

    'maria':{
        'telefono':'9988774455',
        'email':'sol@mail.com',
        'direccion':'sde-471'
    },
    'pedro':{
        'telefono':'4125639874',
        'email':'ser@mail.com',
        'direccion':'hju-523'
    }
}
print(agenda)

# aceder a la informacion de un contacto en especifico
print(f'''informacion de contacto de maria:
        Telefono: {agenda['maria']['telefono']}
        Email: {agenda.get('maria').get('email')}
        Direccion: {agenda.get('maria').get('direccion')}
''')
#agregar nuevo diccionario
agenda['ana']={
    'telefono':'2563147890',
    'email':'get@mail.com',
    'direccion':'lop-147'
}
print(agenda)

#eliminar un contacto existente
agenda.pop('pedro')
#del agenda['pedro']
print(agenda)

# mostrar los contactos de la agenda
print('\nContacto en la agenda:')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    telefono: {detalles.get('telefono')}
    email: {detalles.get('email')}
    direccion: {detalles.get('direccion')}
''')
