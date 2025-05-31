## 🔄 **Bubble Sort (Ordenamiento Burbuja)**

Es un algoritmo de ordenamiento **comparativo** y **simple**, que funciona recorriendo repetidamente una lista, comparando elementos adyacentes y **intercambiándolos si están en el orden incorrecto**. Este proceso se repite hasta que la lista está ordenada.

### 🧠 **Funcionamiento básico**

* Compara dos elementos vecinos.  
* Si están en el orden incorrecto, los intercambia.  
* Después de cada pasada, el elemento más grande "flota" al final de la lista (como una burbuja).  
* Se repite hasta que no hay más intercambios.

---

## ✅ **Ventajas**

* **Fácil de entender e implementar**.  
* No requiere estructuras de datos adicionales (uso en memoria constante O(1)).  
* Puede detectar si la lista ya está ordenada (con una bandera de optimización).  
* Útil para **enseñanza de conceptos básicos de algoritmos** y ordenamiento.

---

## ❌ **Desventajas**

* **Muy ineficiente para listas grandes** (complejidad temporal O(n²) en el peor y promedio de los casos).  
* Realiza muchas comparaciones e intercambios incluso cuando los elementos ya están en orden.  
* Es **superado por algoritmos más eficientes** como Quick Sort, Merge Sort o incluso Insertion Sort en muchos casos.

---

## 📊 **Complejidad**

| Caso                       | Comparaciones | Intercambios | Complejidad             |
|----------------------------|---------------|--------------|--------------------------|
| Mejor (lista ya ordenada) | n - 1         | 0            | O(n) con optimización    |
| Promedio                   | ~n² / 2       | ~n² / 4      | O(n²)                    |
| Peor                       | ~n² / 2       | ~n² / 2      | O(n²)                    |

---

## 📌 Ejemplo de uso:
- Aplicaciones educativas para explicar cómo funcionan los algoritmos de ordenamiento paso a paso.
- Ordenar listas muy cortas, como el reordenamiento visual de elementos en interfaces gráficas pequeñas.
---

## 💡 **Conclusión**

Bubble Sort es más valioso como herramienta educativa que como solución práctica.  
Solo se recomienda para listas pequeñas o cuando la simplicidad del código es más importante que el rendimiento.

## 🛠️ Tecnologías utilizadas

- **Python** para la estructura de la aplicación.

## ❓ Ayuda

Si tienes dudas sobre el contenido o implementación de los códigos, puedes comunicarte a través de la sección de Issues en este repositorio.

## 👥 Autor

- Crystian Muro - Ingeniería de Software 4° "D" UAZ.

---

📌 **Nota:** Este es un proyecto de código abierto. Puedes modificarlo y adaptarlo según tus necesidades.
