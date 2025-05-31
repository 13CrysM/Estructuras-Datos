import time
import random

def bubble(lista, n):
    inicio = time.time()
    
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
    return lista, duracion, comparacion, intercambio

tamaño = int(input("Ingresa el tamaño de la lista a ordenar:  "))
lista = random.sample(range(1, tamaño + 1), tamaño)
print(f"Lista generada:  {lista}")

listaOrd, tiempo, comparaciones, intercambios = bubble(lista, tamaño)
print(f"Lista Ordenada por Bubble: {listaOrd}")
print(f"Tiempo de ordenamiento: {tiempo:.10f} segundos.\nComparaciones: {comparaciones}.\nIntercambios: {intercambios}")