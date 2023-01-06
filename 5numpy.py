import numpy as np

matriz =np.matrix([[2,0,0,0],[0,3,0,0],[0,0,4,0],[0,0,0,5]])
transpuesta = np.transpose(matriz)
def matiz_semitrica(matriz, transpuesta):
  comparacion = np.array_equal(matriz,transpuesta)
  if comparacion is True:
    print("La matriz es simetrica")
    print ("Esta es la matriz original es:", matriz, " \n y esta es su matriz transpuesta es: ", transpuesta, " \ncomo se observa las matrices son iguales.")
  else:
    print ("La matriz no es simetrica:")


print(matiz_semitrica(matriz, transpuesta))