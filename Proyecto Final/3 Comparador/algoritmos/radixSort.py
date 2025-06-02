import time, random

def ordeanar_conteo_digito(arr, exp, stats):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Dígitos del 0 al 9

    # Contar ocurrencias por dígito
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
        stats['comparaciones'] += 1

    # Acumular los conteos
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir la salida estable
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copiar al arreglo original
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    stats = {'comparaciones': 0, 'intercambios': 0}
    start_time = time.time()

    if not arr:
        return 0.0, 0, 0

    max_val = max(arr)
    exp = 1

    # Aplicar Counting Sort para cada dígito
    while max_val // exp > 0:
        ordeanar_conteo_digito(arr, exp, stats)
        exp *= 10

    elapsed_time = time.time() - start_time
    return elapsed_time, stats['comparaciones'], stats['intercambios']
'''
# Lista de enteros positivos
miLista = [random.randint(0, 100000000) for _ in range(1000)]
print(miLista)
tiempo, comparaciones, intercambios = radix_sort(miLista)

print(f"Tiempo de ejecución: {tiempo:.10f} segundos")
print(f"Número de comparaciones simuladas: {comparaciones}")
print(f"Número de intercambios (no aplica): {intercambios}")'''