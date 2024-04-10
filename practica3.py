notas = []
materias = ("Matematica","Literatura","Historia")

for x in range(3):
    nota = int(input(f"Ingrese la nota de {materias[x]}: "))
    notas.append(nota)

def calculo_promedio(notas):
    acumulador = 0
    for x in range(3):
        acumulador += notas[x]
    promedio = acumulador / 3
    return promedio

pro = calculo_promedio(notas)
print("Promedio:", pro)

if (pro > 1.7 and pro < 5 ):
    print("Aprobado, !Felicitaciones¡")
elif (pro == 5 and pro < 5.00000001):
    print("Aprobado, !Excelente Trabajo¡")
elif (pro < 1.7):
    print("Reprobado, !Esfuerzate mas para la proxima¡")
else:
    print("!Valores Invalidos¡")
