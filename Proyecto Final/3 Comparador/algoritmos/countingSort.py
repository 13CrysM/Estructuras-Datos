import time, random

def counting(lista):
    n = len(lista)
    stats = {"comparaciones":0, "intercambios":0}
    inicio = time.time()
    if not lista:
        return [], 0.0, 0, 0

    valorMax = max(lista)
    valorMin = min(lista)
    rango = valorMax - valorMin + 1
    #Contador de frecuencia
    cont = [0] * rango
    salida = [0] * n
    #Contaddor de frecuencia de cada valaor
    for num in lista:
        cont[num - valorMin] += 1
        stats["comparaciones"] += 1 #Como comparación indirecta

    #Acumulación de conteos
    for i in range(1, len(cont)):
        cont[i] += cont[i -1]
    
    #Salida estable
    for num in reversed(lista):
        salida[cont[num - valorMin] - 1] = num
        cont[num - valorMin] -= 1

    #Copiar al arreglo original
    for i in range(n):
        lista[i] = salida[i]
    
    fin = time.time()
    duracion = fin - inicio
    return duracion, stats["comparaciones"], stats["intercambios"]
'''
tamaño = int(input(f"Ingresa el tamaño de la lista: "))
#miLista =  random.sample(range(1, tamaño), tamaño - 1)         #Genera lista con valores únicos
miLista = [random.randint(0, tamaño) for _ in range(tamaño)]    #Genera lista aleatoria
print(f"Lista generada: {miLista}")
listaOrd, tiempo, comparaciones, intercambios  = counting(miLista, tamaño)
print(f"\nLista Ordenada: {listaOrd}")
print(f"Tiempo de ordenamiento: {tiempo:.10f} milisegundos.\nComparaciones: {comparaciones}.\nIntercambios: {intercambios}")'''