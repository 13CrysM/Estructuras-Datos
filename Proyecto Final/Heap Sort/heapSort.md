## 🔄 **Heap Sort (Ordenamiento por Montículo)**

Heap Sort es un algoritmo de ordenamiento comparativo basado en una estructura de datos llamada heap binario (normalmente un max-heap o min-heap). El algoritmo convierte la lista en un heap, y luego extrae el elemento raíz (máximo o mínimo) repetidamente para construir la lista ordenada.

### 🧠 **Funcionamiento básico**
* Se construye un heap máximo desde la lista de entrada.
* El elemento raíz (máximo) se intercambia con el último elemento.
* Se reduce el tamaño del heap y se aplica heapify para restaurar la propiedad de heap.
* Se repite hasta que toda la lista esté ordenada.

---

## ✅ **Ventajas**
* Rendimiento garantizado: siempre tiene complejidad O(n log n), incluso en el peor caso.
* No recursivo por naturaleza: se puede implementar sin recursión (a diferencia de Quick Sort).
* No requiere estructuras adicionales grandes (puede implementarse in-place, es decir, sin memoria adicional significativa).
* No se ve afectado por el orden inicial de los datos.

---

## ❌ **Desventajas**
* **No es estable**: puede cambiar el orden relativo de elementos iguales.
* Menor rendimiento práctico que Quick Sort para la mayoría de los casos.
* Más complejo de implementar correctamente que algoritmos como Insertion Sort o Bubble Sort.

---

## 📊 **Complejidad**

### 📊 **Complejidad**

| Caso       | Comparaciones/Operaciones | Complejidad   |
|------------|----------------------------|---------------|
| Mejor      | O(n log n)                 | O(n log n)    |
| Promedio   | O(n log n)                 | O(n log n)    |
| Peor       | O(n log n)                 | O(n log n)    |
| Espacio    | O(1) (in-place)            | —             |

---

## 💡 **Conclusión**
Heap Sort es un algoritmo robusto con buen rendimiento en el peor caso y bajo uso de memoria.
Aunque no es el más rápido en la práctica, es útil cuando se necesita una ordenación eficiente, confiable y sin memoria adicional. Ideal para aplicaciones con restricciones de espacio y necesidad de consistencia en el tiempo de ejecución.

## 🛠️ Tecnologías utilizadas

- **Python** para la estructura de la aplicación.

## ❓ Ayuda

Si tienes dudas sobre el contenido o implementación de los códigos, puedes comunicarte a través de la sección de Issues en este repositorio.

## 👥 Autor

- Crystian Muro - Ingeniería de Software 4° "D" UAZ.

---

📌 **Nota:** Este es un proyecto de código abierto. Puedes modificarlo y adaptarlo según tus necesidades.
