import numpy as np
matriz =np.matrix([[2,3,1],[4,3,5],[5,6,7]])
matriz1 =np.matrix([[5,5,6],[0,-2,6],[8,-1,-2]])
#suma de una matriz
suma= matriz + matriz1
#resta de una matriz
resta = matriz - matriz
#multiplición  de una matriz
producto=np.dot(matriz,matriz1) 
print('las matrices son: \n' , matriz , matriz1) 
print('la suma de la matrices es: \n', suma)
print('la resta de la matrices es: \n', resta)
print('el producto de las matrices es: \n', producto)