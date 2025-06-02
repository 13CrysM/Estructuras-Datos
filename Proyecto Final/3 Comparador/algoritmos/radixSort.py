import time, random

def ordeanar_conteo_digito(lista, exp, stats):
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10  # Dígitos del 0 al 9

    # Contar ocurrencias por dígito
    for i in range(n):
        indice = (lista[i] // exp) % 10
        conteo[indice] += 1
        stats['comparaciones'] += 1

    # Acumular los conteos
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construir la salida estable
    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1
        i -= 1

    # Copiar al listaeglo original
    for i in range(n):
        lista[i] = salida[i]


def radix(lista):
    stats = {'comparaciones': 0, 'intercambios': 0}
    start_time = time.time()

    if not lista:
        return 0.0, 0, 0

    max_val = max(lista)
    exp = 1

    # Aplicar Counting Sort para cada dígito
    while max_val // exp > 0:
        ordeanar_conteo_digito(lista, exp, stats)
        exp *= 10

    elapsed_time = time.time() - start_time
    return lista, elapsed_time, stats['comparaciones'], stats['intercambios']
'''
# Lista de enteros positivos
miLista = [random.randint(0, 100000000) for _ in range(1000)]
print(miLista)
tiempo, comparaciones, intercambios = radix_sort(miLista)

print(f"Tiempo de ejecución: {tiempo:.10f} segundos")
print(f"Número de comparaciones simuladas: {comparaciones}")
print(f"Número de intercambios (no aplica): {intercambios}")'''