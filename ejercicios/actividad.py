canEst=int(input("ingrese la cantidad de estudiantes"))
promedio=0
for i in range(canEst):
    print("informacion estudiante ", i)
    actividad1=float(input("ingrese la nota de la actividad 1"))
    actividad2=float(input("ingrese la nota de la actividad 2"))
    actividad3=float(input("ingrese la nota de la actividad 3"))
    notaFinal=(actividad1*.5)+(actividad2*.25)+(actividad3*.25)
    print("la nota final del estudiante", i, "es ",notaFinal)
    promedio=promedio+notaFinal
promedio=promedio/canEst
print("el promedio es: ",promedio)