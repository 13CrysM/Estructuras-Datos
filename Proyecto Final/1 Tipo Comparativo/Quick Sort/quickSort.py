import time
import random

def quick(lista):
    stats = {'comparaciones': 0, 'intercambios': 0}
    inicio = time.time()

    def particion(menor, mayor):
        pivot = lista[mayor]  # Usamos el último elemento como pivote
        i = menor - 1  # Índice del menor elemento

        for j in range(menor, mayor):
            stats['comparaciones'] += 1
            if lista[j] <= pivot:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
                stats['intercambios'] += 1

        # Coloca el pivote en su posición final
        lista[i + 1], lista[mayor] = lista[mayor], lista[i + 1]
        stats['intercambios'] += 1
        return i + 1

    def ordenar(menor, mayor):
        if menor < mayor:
            pi = particion(menor, mayor)  # Índice de partición
            ordenar(menor, pi - 1)  # Ordena sublista izquierda
            ordenar(pi + 1, mayor)  # Ordena sublista derecha

    ordenar(0, len(lista) - 1)
    fin = time.time()
    duracion = fin - inicio
    return lista, duracion, stats['comparaciones'], stats['intercambios']

tamaño = int(input(f"Ingresa el tamaño de la lista: "))
#miLista =  random.sample(range(1, tamaño), tamaño - 1)         #Genera lista con valores únicos
miLista = [random.randint(1, tamaño) for _ in range(tamaño)]    #Genera lista aleatoria
print(f"Lista generada: {miLista}")
listaOrd, tiempo, comparaciones, intercambios  = quick(miLista)
print(f"\nLista Ordenada: {listaOrd}")
print(f"Tiempo de ordenamiento: {tiempo:.10f} segundos.\nComparaciones: {comparaciones}.\nIntercambios: {intercambios}")