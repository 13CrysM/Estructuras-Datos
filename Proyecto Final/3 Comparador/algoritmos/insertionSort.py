import time
import random

def insertion(lista):
    n = len(lista)
    inicio = time.time()
    stats = {"comparaciones":0, "intercambios":0}
    for i in range(1, n):
        pivote = lista[i]   #Se toma el segundo elemento de la lista como punto de partida
        j = i - 1
        while j >= 0: #Comparación y desplazamiento
            stats["comparaciones"] += 1
            if lista [j] > pivote:
                lista[j + 1] = lista[j]
                stats["intercambios"] += 1
                j -= 1
            else:
                break
        # Se posiciona en el lugar correcto
        lista[j + 1] = pivote
        stats["intercambios"] += 1

    fin = time.time()
    duracion = fin - inicio
    return duracion, stats["comparaciones"], stats["intercambios"]

'''tamaño = int(input(f"Ingresa el tamaño de la lista: "))
#miLista =  random.sample(range(1, tamaño), tamaño - 1)         #Genera lista con valores únicos
miLista = [random.randint(1, tamaño) for _ in range(tamaño)]    #Genera lista aleatoria
print(f"Lista generada: {miLista}")
listaOrd, tiempo, comparaciones, intercambios  = insertion(miLista, tamaño)
print(f"\nLista Ordenada: {listaOrd}")
print(f"Tiempo de ordenamiento: {tiempo:.10f} segundos.\nComparaciones: {comparaciones}.\nIntercambios: {intercambios}")'''