####################################
### Version Final ##################
### Algoritmo Gauss Jordan #########
# file: SolucionadorEcuacionesLineales.py

## Miembros del equipo: 
## Crystian Muro
## Arely Sanchez
## Juan Noriega
import numpy as np

def gauss_jordan(matrix):
    """
    Resuelve un sistema de ecuaciones utilizando el método de Gauss-Jordan.
    :param matrix: Una matriz aumentada que representa el sistema de ecuaciones.
    :return: La matriz resultante con la solución.
    """
    rows, cols = len(matrix), len(matrix[0])
    tieneSolucion = True

    for i in range(rows):
      pivot = matrix[i][i]
      for j in range(cols):
          print(pivot)
          matrix[i][j] /= pivot
      for k in range(rows):
          if k != i:
              factor = matrix[k][i]
              for j in range(cols):
                  matrix[k][j] -= factor * matrix[i][j]
                  print("k=",k,"j=",j,"rows=",rows,"cols=",cols,"valor=",matrix[k][j-1],matrix[k][j])
      if j == cols-1 and matrix[k][j-1] == 0 and matrix[k][j] != 0:
          tieneSolucion = False
          break
    print(matrix)
    return (tieneSolucion, matrix)

def pedir_matrix():
    n = int(input("cuantas incognitas tiene el sistema de ecuaciones? "))
    matrix = np.zeros((n,n+1))
    print("Ingresa los coeficientes de la matriz aumentada.")
    for i in range (n):
      for j in range (n+1):
        matrix[i][j] = float(input('matriz['+str(i)+']['+ str(j)+']='))
    return matrix

def intercambiar_renglones(matrix):
    n = len(matrix)
    for i in range(n):
        # verificar si el elemento en la diagonal principal es cero
        if matrix[i][i] == 0:
            # buscar un renglón debajo del actual que tenga un elemento no cero en la misma columna
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    # intercambia los elementos de los renglones
                    for k in range(n+1):
                        matrix[i][k], matrix[j][k] = matrix[j][k], matrix[i][k]
                    break
    for row in matrix:
       print(row, "row")
    return matrix

def fixMatrixRows(matrix, i):
  indice = 0
  for row in matrix:
    if row[i] != 0.0:
      break
    indice += 1
  
  temp = matrix[i].copy()
  matrix[i] = matrix[indice]
  matrix[indice] = temp
  for row in matrix:
        print(row)
  return matrix

# Ejemplo de uso
if __name__ == "__main__":
    # pregunta al usuario la matriz aumentada del sistema de ecuaciones
    matriz = pedir_matrix()
    matriz = intercambiar_renglones(matriz)
    # Resuelve el sistema
    bandera, solucion = gauss_jordan(matriz)
    # Imprime solución
    if bandera == True:
      print("La solución del sistema de ecuaciones es:")
      for row in solucion:
        print(row)
    else:
      print("El sistema no tiene solucion")
      for row in solucion:
        print(row)