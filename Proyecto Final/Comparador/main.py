from algoritmos import bubleSort,countingSort,heapSort,insertionSort,mergeSort, quickSort, radixSort, selectionSort
from utils.generador_lista import generar_lista
from utils.graficador import graficar_resultados

# Tamaño de la lista
n = 1000
lista_base = generar_lista(n)

# Diccionario para guardar resultados
resultados = {}

# Lista de algoritmos y sus funciones
algoritmos = {
    "Bubble Sort": bubleSort.bubble,
    "Insertion Sort": insertionSort.insertion,
    "Selection Sort": selectionSort.selection,
    "Merge Sort": mergeSort.mergeSort,
    "Quick Sort": quickSort.quick,
    "Heap Sort": heapSort.heapSort,
    "Counting Sort": countingSort.counting,
    "Radix Sort": radixSort.radix_sort
}

# Ejecutar todos los algoritmos
for nombre, funcion in algoritmos.items():
    lista_copia = lista_base.copy()
    #print(f"copia{lista_copia}")
    tiempo, comparaciones, intercambios = funcion(lista_copia)
    resultados[nombre] = {
        'tiempo': tiempo,
        'comparaciones': comparaciones,
        'intercambios': intercambios
    }

# Mostrar resultados en gráfica
graficar_resultados(resultados)
