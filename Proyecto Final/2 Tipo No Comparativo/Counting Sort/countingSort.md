## 🔄 **Counting Sort (Ordenamiento por Conteo)**

**Counting Sort** es un algoritmo de ordenamiento no comparativo, ideal para listas de enteros en un rango conocido. En lugar de comparar elementos, **cuenta cuántas veces aparece cada valor** y reconstruye la lista ordenada a partir de esas frecuencias.


### 🧠 **Funcionamiento básico**

1. Encuentra el **valor máximo** en la lista.
2. Crea un arreglo de conteo de tamaño `max + 1`.
3. Cuenta la frecuencia de cada valor.
4. Acumula los conteos para determinar posiciones finales.
5. Construye la lista ordenada con base en el arreglo de conteo.

---

## ✅ **Ventajas**

- Extremadamente rápido: **O(n + k)** donde `k` es el rango de valores.
- No utiliza comparaciones entre elementos.
- Muy eficiente para **enteros pequeños o con rango limitado**.

---

## ❌ **Desventajas**

- Solo funciona con **enteros no negativos**.
- Requiere **memoria adicional proporcional al rango (`k`)**.
- Ineficiente si el rango es muy grande en comparación al número de elementos.
- No es ideal para tipos de datos como flotantes o cadenas (sin modificaciones).

---
## 📌 Ejemplo de uso:
- Ordenar edades de personas en un censo (rango limitado).
- Clasificar puntuaciones de exámenes escolares donde los valores están entre 0 y 100.
---
## 📊 **Complejidad**

| Caso       | Complejidad     | Descripción                                |
|------------|------------------|--------------------------------------------|
| Mejor      | O(n + k)         | `n`: tamaño de la lista, `k`: valor máximo |
| Promedio   | O(n + k)         | Eficiente si `k` no es muy grande          |
| Peor       | O(n + k)         | Consistente sin importar el orden          |
| Espacio    | O(k + n)         | Arreglo de conteo + salida ordenada        |
---

## 💡 **Conclusión**

**Counting Sort** es uno de los algoritmos más rápidos para listas de enteros con un rango reducido. Aunque no es versátil, es excelente para aplicaciones específicas como clasificación de edades, conteo de frecuencias o sistemas integrados.

## 🛠️ Tecnologías utilizadas

- **Python** para la estructura de la aplicación.

## ❓ Ayuda

Si tienes dudas sobre el contenido o implementación de los códigos, puedes comunicarte a través de la sección de Issues en este repositorio.

## 👥 Autor

- Crystian Muro - Ingeniería de Software 4° "D" UAZ.

---

📌 **Nota:** Este es un proyecto de código abierto. Puedes modificarlo y adaptarlo según tus necesidades.
