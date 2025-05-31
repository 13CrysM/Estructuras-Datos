## 🔄 **Insertion Sort (Ordenamiento Inserción)**

**Insertion Sort** es un algoritmo de ordenamiento comparativo que construye la lista ordenada de izquierda a derecha, insertando cada nuevo elemento en la posición correcta dentro de la parte ya ordenada. Es similar a cómo se ordenan las cartas en la mano.


### 🧠 **Funcionamiento básico**

* Comienza desde el segundo elemento.
* Compara hacia atrás con los elementos ya ordenados.
* Desplaza hacia la derecha los mayores que él.
* Inserta el elemento actual en su lugar correcto.

---

## ✅ **Ventajas**

- **Fácil de implementar** y entender.
- **Eficiente para listas pequeñas** o casi ordenadas.
- **Estable**: no cambia el orden de los elementos iguales.
- **In-place**: no requiere memoria adicional significativa.

---

## ❌ **Desventajas**

- **Ineficiente para listas grandes** o desordenadas.
- Número de comparaciones e intercambios puede ser alto en el peor caso.

---
### 📌 Ejemplo de uso:
- Ordenar listas de contactos cuando solo se agrega un nuevo contacto a una lista ya ordenada.
- Aplicaciones en tiempo real donde los datos se reciben uno a uno y se ordenan al momento.
---
## 📊 **Complejidad**
| Caso       | Comparaciones/Movimientos | Complejidad   |
|------------|----------------------------|---------------|
| Mejor      | O(n)                       | Lista ya ordenada |
| Promedio   | O(n²)                      | Orden aleatorio   |
| Peor       | O(n²)                      | Lista en orden inverso |
| Espacio    | O(1)                       | In-place       |

## 💡 **Conclusión**
**Insertion Sort** es ideal para listas pequeñas o parcialmente ordenadas.  
Aunque no es adecuado para grandes volúmenes de datos debido a su rendimiento cuadrático, su sencillez y eficiencia en casos simples lo hacen útil en contextos educativos y optimizaciones internas de otros algoritmos.


## 🛠️ Tecnologías utilizadas

- **Python** para la estructura de la aplicación.

## ❓ Ayuda

Si tienes dudas sobre el contenido o implementación de los códigos, puedes comunicarte a través de la sección de Issues en este repositorio.

## 👥 Autor

- Crystian Muro - Ingeniería de Software 4° "D" UAZ.

---

📌 **Nota:** Este es un proyecto de código abierto. Puedes modificarlo y adaptarlo según tus necesidades.
