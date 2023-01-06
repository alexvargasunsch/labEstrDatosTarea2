import numpy as np

matriz1 =np.matrix([[2,7,8],[4,8,-2],[7,1,0]])
def determinate_matriz(matriz):
    determinante = np.linalg.det(matriz)
    return determinante

respuesta= determinate_matriz(matriz1)
print('La matriz a calcular su determinate es:\n', matriz1 ,'\n y su determinate es: \n'
, int(respuesta))
