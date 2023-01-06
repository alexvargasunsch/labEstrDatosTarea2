def array(tamaño, multiplo):
    array = []
    for i in range (0,tamaño):
        respuesta = array.append(i*multiplo)
    return respuesta

tamaño = int(input("Ingrese el tamaño del array: "))
multiplo = int(input("Ingrese el número de múltiplos: "))

arreglo = array(tamaño, multiplo)
print (arreglo)