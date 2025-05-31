import random

def generar_lista(tamano, max_valor=10000):
    return [random.randint(0, max_valor) for _ in range(tamano)]