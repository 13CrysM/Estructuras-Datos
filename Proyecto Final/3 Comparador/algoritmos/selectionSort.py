import time
import random

def selection(lista):
    n = len(lista)
    stats = {"comparaciones":0, "intercambios":0}
    inicio = time.time()
    for i in range(n):
        indiceMenor = i
        for j in range(i + 1, n):
            stats["comparaciones"] += 1
            if lista[j] < lista[indiceMenor]:
                indiceMenor = j
        if indiceMenor != i:
            lista[i], lista[indiceMenor] = lista[indiceMenor], lista[i]
            stats["intercambios"] += 1
    fin = time.time()
    duracion = fin - inicio

    return duracion, stats["comparaciones"], stats["intercambios"]


'''
tamaño = int(input(f"Ingresa el tamaño de la lista: "))
#miLista =  random.sample(range(1, tamaño), tamaño - 1)         #Genera lista con valores únicos
miLista = [random.randint(0, tamaño) for _ in range(tamaño)]    #Genera lista aleatoria
print(f"Lista generada: {miLista}")
listaOrd, tiempo, comparaciones, intercambios  = selection(miLista, tamaño)
print(f"\nLista Ordenada: {listaOrd}")
print(f"Tiempo de ordenamiento: {tiempo:.10f} segundos.\nComparaciones: {comparaciones}.\nIntercambios: {intercambios}")'''