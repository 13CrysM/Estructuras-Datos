import time
import random

def amontonar(lista, n, i, stats):
    largo = i
    izquierdo = 2 * i + 1
    derecho = 2 * i +2
    #Compara con hijo izquierdo
    if izquierdo < n:
        stats["comparaciones"] += 1 #Diccionario para almacenar estadistica de comparaciones
        if lista[izquierdo] > lista[largo]:
            largo = izquierdo
    #Compara con hijo derecho
    if derecho < n:
            stats["comparaciones"] += 1 #Diccionario para almacenar estadistica de comparaciones
            if lista[derecho] > lista[largo]:
                largo = derecho
    # Si el mayor no es la raíz
    if largo != i:
        lista[i], lista[largo] = lista[largo], lista[i]
        stats['intercambios'] += 1
        amontonar(lista, n, largo, stats)

def heapSort(lista):
    n = len(lista)
    stats = {"comparaciones": 0, "intercambios": 0}
    inicio = time.time()
    #Construir un 'montón' máximo
    for i in range(n // 2-1 ,-1, -1):
        amontonar(lista, n, i, stats)
    #Extraer elementos uno por vez
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0] #Se mueve la raíz hasta el final
        stats["intercambios"] += 1
        amontonar(lista, i, 0, stats)

    fin = time.time()
    duracion = fin - inicio
    return duracion, stats["comparaciones"], stats["intercambios"]

'''tamaño = int(input("Ingresa el tamaño de la lista: "))
#miLista =  random.sample(range(1, tamaño), tamaño - 1)         #Genera lista con valores únicos
miLista = [random.randint(1, tamaño) for _ in range(tamaño)]    #Genera lista aleatoria
print(f"Lista generada: {miLista}")

listaOrd, tiempo, comparaciones, intercambios = heapSort(miLista, tamaño)
print(f"Lista Ordenada por Bubble: {listaOrd}")
print(f"Tiempo de ordenamiento: {tiempo:.10f} segundos.\nComparaciones: {comparaciones}.\nIntercambios: {intercambios}")'''