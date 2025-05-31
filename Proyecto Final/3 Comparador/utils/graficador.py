import matplotlib.pyplot as plt

def graficar_resultados(resultados):
    algoritmos = list(resultados.keys())
    tiempos = [resultados[alg]['tiempo'] for alg in algoritmos]
    comparaciones = [resultados[alg]['comparaciones'] for alg in algoritmos]
    intercambios = [resultados[alg]['intercambios'] for alg in algoritmos]

    x = range(len(algoritmos))

    plt.figure(figsize=(12, 6))

    # Tiempo
    plt.subplot(1, 3, 1)
    plt.bar(x, tiempos, color='skyblue')
    plt.title('Tiempo de ejecución (s)')
    plt.xticks(x, algoritmos, rotation=45, ha='right')

    # Comparaciones
    plt.subplot(1, 3, 2)
    plt.bar(x, comparaciones, color='lightgreen')
    plt.title('Comparaciones')
    plt.xticks(x, algoritmos, rotation=45, ha='right')

    # Intercambios
    plt.subplot(1, 3, 3)
    plt.bar(x, intercambios, color='salmon')
    plt.title('Intercambios')
    plt.xticks(x, algoritmos, rotation=45, ha='right')

    plt.tight_layout()
    plt.show()
