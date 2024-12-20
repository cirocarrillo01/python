#----practica 2--------
#-----------------------------------------
def new_game():
    respuestas = []
    respuestas_correctas = 0
    pregunta_num = 0
    
    for key in preguntas:
        print('----------------------------------------------')
        print(key)
        for i in opciones[pregunta_num]:
            print(i)
            
        respuesta = input('ingresa (A, B, C, D): ').upper()
        respuestas.append(respuesta)
        
        respuestas_correctas += check_answer(preguntas.get(key), respuesta)
        pregunta_num +=1
        
    display_score(respuestas_correctas, respuestas)
#-----------------------------------------
def check_answer(respuesta_correcta, respuesta):
    
    if respuesta_correcta == respuesta:
        print('CORRECTA')
        return 1
    else:
        print('INCORRECTO')
        return 0
#-----------------------------------------
def display_score(respuestas_correctas, respuestas):
    print('--------------------------------------')
    print('RESULTADO')
    print('--------------------------------------')
    
    print('respuesta correcta: ', end=' ')
    for i in preguntas:
        print(preguntas.get(i), end=' ')
    print()
    
    print('tus respuestas: ', end=' ')
    for i in respuestas:
        print(i, end=' ')
    print()
    
    puntaje = int((respuestas_correctas/len(preguntas))*100)
    print('puntaje: '+ str(puntaje) + ' %')
#-----------------------------------------
def paly_again():
    respuesta = input('quiers jugar de nuevo: (SI/NO) ').upper()
    
    if respuesta == 'SI':
        return True
    else:
        return False
#-----------------------------------------


preguntas = {
    '¿Que idioma se habla en brasil?: ':'A',
    '¿Cual es el oceano mas grande del mundo?: ':'B',
    '¿Cual es la estrella mas cercana a la tierra?: ':'C',
    'Cual es la segundo pais mas grande del mundo?: ':'A',
}

opciones = [['A. Portugues','B. Español','C. brasilero','D. Ingles'],
            ['A. Atlantico','B. Pacifico','C. Artico','D. Indico'],
            ['A. La Luna','B. Alfa centauri','C. El sol','D. Ninguna'],
            ['A. Canada','B. Rusia','C. EE.UU','D. China']]


new_game()

while paly_again():
    new_game()
    
print('adios!!')
