def eliminarMinima(lista):
    min = 100
    for elemento in (lista):
        if elemento<min:
            min = elemento
    lista.remove(min)
    print("La nota minima es : ",min)
    return lista
def promedioNotas(lista):
    suma = 0
    n = 0
    for elemento in (lista):
        suma+= elemento
        n+= 1
    promedio = float(suma/n)
    return promedio

notas = [15,15,13,11,14]
notafinal = eliminarMinima(notas)
promedio = promedioNotas(notafinal)
print("El promedio de notas es : ", promedio)