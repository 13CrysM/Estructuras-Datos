import time
import random

def bubble(lista):
    inicio = time.time()
    n = len(lista)
    comparacion = 0
    intercambio = 0
    for i in range(n):
        bandera = False     # Bandera para detectar si hay intercambios
        for j in range(0, n - i - 1):
            comparacion += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio += 1
                bandera  = True
        if not bandera:
            break # Si no hay intercambios
    fin = time.time()
    duracion = fin - inicio
    #print(f"Lista Ordenada(f): {lista}")
    return duracion, comparacion, intercambio
'''
listSize = int(input("Ingresa el tamaño de la lista a ordenar:  "))
lista = random.sample(range(1, listSize + 1), listSize)
print(f"Lista generada:  {lista}")

listaOrd, tiempo, comparaciones, intercambios = bubble(lista)
print(f"Lista Ordenada por Bubble: {listaOrd}")
print(f"Tiempo de ordenamiento: {tiempo:.10f} segundos.\nComparaciones: {comparaciones}.\nIntercambios: {intercambios}")'''