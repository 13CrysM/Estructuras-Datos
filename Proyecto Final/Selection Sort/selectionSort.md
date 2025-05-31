## 🔄 **Bubble Sort (Ordenamiento Burbuja)**

**Selection Sort** es un algoritmo de ordenamiento simple y comparativo. Su idea principal es encontrar el elemento mínimo (o máximo) de una lista y colocarlo en su posición correcta, repitiendo este proceso para cada elemento restante.

### 🧠 **Funcionamiento básico**

* Recorre toda la lista para encontrar el **mínimo**.
* Intercambia ese mínimo con el elemento en la primera posición.
* Repite el proceso desde la siguiente posición hasta el final.

---

## ✅ **Ventajas**
- Muy fácil de implementar.
- No requiere memoria adicional (es in-place).
- Bueno para listas pequeñas o ya parcialmente ordenadas.

---

## ❌ **Desventajas**
- Ineficiente en listas grandes: realiza muchas comparaciones.
- No es estable (puede cambiar el orden relativo de elementos iguales).
- Siempre realiza el mismo número de comparaciones, esté ordenada o no.

---

## 📊 **Complejidad**

| Caso       | Complejidad     | Descripción                                  |
|------------|------------------|----------------------------------------------|
| Mejor      | O(n²)            | Siempre hace n²/2 comparaciones              |
| Promedio   | O(n²)            | Independiente del orden de los datos         |
| Peor       | O(n²)            | Igual número de comparaciones e intercambios |
| Espacio    | O(1)             | No usa memoria adicional                     |
---

## 💡 **Conclusión**

**Selection Sort** es útil cuando el número de intercambios debe minimizarse, pero es muy lento comparado con algoritmos como Merge o Quick Sort. Se usa más como herramienta educativa que en entornos reales de producción.

## 🛠️ Tecnologías utilizadas

- **Python** para la estructura de la aplicación.

## ❓ Ayuda

Si tienes dudas sobre el contenido o implementación de los códigos, puedes comunicarte a través de la sección de Issues en este repositorio.

## 👥 Autor

- Crystian Muro - Ingeniería de Software 4° "D" UAZ.

---

📌 **Nota:** Este es un proyecto de código abierto. Puedes modificarlo y adaptarlo según tus necesidades.
