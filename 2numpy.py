import numpy as np
matriz =np.matrix([[2,3,1,6],[4,3,5,7],[5,6,7,0],[8,9,0,0]])
matriz1 =np.matrix([[5,5,6,50],[0,-2,5,6],[0,8,-1,-2],[6,7,9,-1]])
producto=np.dot(matriz,matriz1) 
print('las matrices son: \n' , matriz , matriz1)
print('el producto de las matrices es: \n', producto)