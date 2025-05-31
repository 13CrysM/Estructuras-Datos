## 🔄 **Merge Sort (Ordenamiento por mezcla)**

**Merge Sort** es un algoritmo de ordenamiento comparativo basado en el paradigma **Divide y vencerás**. Divide la lista en mitades recursivamente hasta que cada sublista tiene un solo elemento, y luego las mezcla (merge) en forma ordenada.



### 🧠 **Funcionamiento básico**

* Dividir: la lista se divide recursivamente en mitades.
* Conquistar: cada sublista se ordena recursivamente.
* Combinar: las sublistas ordenadas se fusionan para producir una lista final ordenada.

---

## ✅ **Ventajas**

- **Eficiente** para grandes volúmenes de datos.
- **Complejidad constante O(n log n)** en todos los casos.
- **Estable**: mantiene el orden relativo de elementos iguales.
- Es útil en estructuras que no permiten acceso aleatorio (como listas enlazadas).

---

## ❌ **Desventajas**
- Requiere **memoria adicional** proporcional al tamaño de la lista (no es in-place).
- Puede ser más lento en listas pequeñas que algoritmos simples como Insertion Sort.

---

## 📊 **Complejidad**

| Caso       | Complejidad     | Descripción                                |
|------------|------------------|--------------------------------------------|
| Mejor      | O(n log n)       | Siempre divide la lista eficientemente     |
| Promedio   | O(n log n)       | No depende de la distribución de datos     |
| Peor       | O(n log n)       | Incluso en el peor caso se mantiene estable|
| Espacio    | O(n)             | Requiere almacenamiento adicional          |

---

## 💡 **Conclusión**

**Merge Sort** es una excelente opción cuando se requiere rendimiento garantizado sin importar la distribución de los datos. Su uso es común en algoritmos internos de bibliotecas estándar y para ordenar archivos grandes.


## 🛠️ Tecnologías utilizadas

- **Python** para la estructura de la aplicación.

## ❓ Ayuda

Si tienes dudas sobre el contenido o implementación de los códigos, puedes comunicarte a través de la sección de Issues en este repositorio.

## 👥 Autor

- Crystian Muro - Ingeniería de Software 4° "D" UAZ.

---

📌 **Nota:** Este es un proyecto de código abierto. Puedes modificarlo y adaptarlo según tus necesidades.
