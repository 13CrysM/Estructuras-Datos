## 🔄 **Radix Sort (Ordenamiento por radix o base)**

**Radix Sort** es un algoritmo no comparativo que ordena los números procesando dígito por dígito, comenzando por el menos significativo (LSD - Least Significant Digit) o el más significativo (MSD). Utiliza un algoritmo estable como Counting Sort como subrutina.


### 🧠 **Funcionamiento básico**

1. Encuentra el número con más dígitos.
2. Ordena todos los números por cada dígito, desde el menos significativo al más significativo.
3. Para cada dígito, aplica un ordenamiento **estable** como Counting Sort.

---

## ✅ **Ventajas**

- Muy eficiente para ordenar enteros grandes cuando los valores no son muy dispersos.
- No depende de comparaciones.
- Puede ser más rápido que algoritmos O(n log n) en ciertas condiciones.

---

## ❌ **Desventajas**
- Solo funciona con **enteros no negativos** (o necesita ajustes para negativos).
- Requiere una función de ordenamiento estable por dígito.
- No es tan versátil como Merge o Quick Sort.
- Consumo de memoria adicional proporcional al número de dígitos y elementos.

---

## 📊 **Complejidad**

| Caso       | Complejidad     | Descripción                                 |
|------------|------------------|---------------------------------------------|
| Mejor      | O(nk)            | `k`: número de dígitos                      |
| Promedio   | O(nk)            | Muy eficiente si `k` es pequeño             |
| Peor       | O(nk)            | Lineal respecto al tamaño y longitud        |
| Espacio    | O(n + k)         | Requiere memoria adicional                  |
---

## 💡 **Conclusión**

**Radix Sort** es una excelente opción para listas grandes de enteros positivos con un número limitado de dígitos. Si se combina con un ordenamiento estable y eficiente, puede superar a algoritmos comparativos en muchos escenarios.

## 🛠️ Tecnologías utilizadas

- **Python** para la estructura de la aplicación.

## ❓ Ayuda

Si tienes dudas sobre el contenido o implementación de los códigos, puedes comunicarte a través de la sección de Issues en este repositorio.

## 👥 Autor

- Crystian Muro - Ingeniería de Software 4° "D" UAZ.

---

📌 **Nota:** Este es un proyecto de código abierto. Puedes modificarlo y adaptarlo según tus necesidades.
