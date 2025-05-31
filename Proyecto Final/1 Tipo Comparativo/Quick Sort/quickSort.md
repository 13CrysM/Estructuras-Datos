## 🔄 **Quick Sort (Ordenamiento Rápido)**

**Quick Sort** es un algoritmo de ordenamiento comparativo basado en el enfoque **Divide y vencerás**. Selecciona un elemento como *pivote* y particiona el resto de la lista en elementos menores o mayores que el pivote, ordenando recursivamente cada sublista.


### 🧠 **Funcionamiento básico**

1. Elegir un **pivote** (puede ser el primer, último, medio o aleatorio).
2. Particionar la lista en dos sublistas:
   - Elementos menores o iguales al pivote.
   - Elementos mayores al pivote.
3. Aplicar Quick Sort recursivamente a ambas sublistas.

---

## ✅ **Ventajas**

- Rendimiento **muy pobre en el peor caso**: **O(n²)** si el pivote se elige mal.
- **No es estable** (puede cambiar el orden de elementos iguales).
- Puede requerir optimizaciones para grandes listas (como usar mediana o random pivot).

---

## ❌ **Desventajas**

* **Muy ineficiente para listas grandes** (complejidad temporal O(n²) en el peor y promedio de los casos).  
* Realiza muchas comparaciones e intercambios incluso cuando los elementos ya están en orden.  
* Es **superado por algoritmos más eficientes** como Quick Sort, Merge Sort o incluso Insertion Sort en muchos casos.

---
## 📌 Ejemplo de uso:
- Sistemas que requieren ordenamiento rápido en memoria como bases de datos en RAM.
- Aplicaciones de búsqueda como motores de búsqueda o compiladores.
---
## 📊 **Complejidad**

| Caso       | Complejidad     | Descripción                                       |
|------------|------------------|---------------------------------------------------|
| Mejor      | O(n log n)       | Partición equilibrada                             |
| Promedio   | O(n log n)       | Elección aleatoria o adecuada del pivote          |
| Peor       | O(n²)            | Lista ya ordenada o pivote mal elegido            |
| Espacio    | O(log n)         | Uso de pila por recursión (sin memoria adicional) |

---

## 💡 **Conclusión**

**Quick Sort** es uno de los algoritmos más rápidos y populares. Su rendimiento excelente en la mayoría de los casos lo hace ideal para sistemas donde se prioriza la velocidad. Sin embargo, es importante considerar su peor caso y estabilidad.

## 🛠️ Tecnologías utilizadas

- **Python** para la estructura de la aplicación.

## ❓ Ayuda

Si tienes dudas sobre el contenido o implementación de los códigos, puedes comunicarte a través de la sección de Issues en este repositorio.

## 👥 Autor

- Crystian Muro - Ingeniería de Software 4° "D" UAZ.

---

📌 **Nota:** Este es un proyecto de código abierto. Puedes modificarlo y adaptarlo según tus necesidades.
