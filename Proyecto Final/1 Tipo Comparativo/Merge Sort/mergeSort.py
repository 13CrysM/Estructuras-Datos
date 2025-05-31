import time
import random
def mergeSort(lista):
    stats = {"comparaciones":0, "intercambios":0}
    inicio = time.time()

    def mezcla(izquierda, derecha):
        listaMezclada = []
        i = j = 0   #indices para recorrido de izquierda y derecha

        while i < len(izquierda) and j < len(derecha):
            stats["comparaciones"] += 1
            if izquierda[i] <= derecha[j]:
                listaMezclada.append(izquierda[i])  #Agrega el menor
                i += 1
            else:
                listaMezclada.append(derecha[j])
                j += 1
            stats["intercambios"] += 1
        while i < len(izquierda):
            listaMezclada.append(izquierda[i])
            i += 1
            stats["intercambios"] += 1
        while j < len(derecha):
            listaMezclada.append(derecha[j])
            j += 1
            stats["intercambios"] += 1
        return listaMezclada
    
    
    def ordena(listaAlterna):
        """
        Función recursiva que divide el arreglo hasta sublistas de un elemento
        y luego las fusiona ordenadamente con merge().
        """
        if len(listaAlterna) <= 1:
            return listaAlterna  # Base de la recursión

        mid = len(listaAlterna) // 2  # Mitad del arreglo
        left = ordena(listaAlterna[:mid])   # Ordenar recursivamente la mitad izquierda
        right = ordena(listaAlterna[mid:])  # Ordenar recursivamente la mitad derecha

        return mezcla(left, right)  # Fusionar las mitades ordenadas
    
    ordLista = ordena(lista)
    fin = time.time()
    duracion = fin - inicio
    lista [:] = ordLista
    
    return ordLista, duracion, stats["comparaciones"], stats["intercambios"]

tamaño = int(input(f"Ingresa el tamaño de la lista: "))
#miLista =  random.sample(range(1, tamaño), tamaño - 1)         #Genera lista con valores únicos
miLista = [random.randint(1, tamaño) for _ in range(tamaño)]    #Genera lista aleatoria
print(f"Lista generada: {miLista}")
listaOrd, tiempo, comparaciones, intercambios  = mergeSort(miLista)
print(f"\nLista Ordenada: {listaOrd}")
print(f"Tiempo de ordenamiento: {tiempo:.10f} segundos.\nComparaciones: {comparaciones}.\nIntercambios: {intercambios}")