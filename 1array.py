tamaño = int(input(u"Ingrese el tamaño del arreglo: "))
array1 = []
array2 = []

for i in range(tamaño):
    array1.append(input("Ingrese un nombre: "))
print(array1)

for x in range(tamaño):
    array2.append(len(array1[x]))
print(array2)