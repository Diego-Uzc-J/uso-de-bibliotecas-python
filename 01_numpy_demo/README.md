# Demostración de NumPy: Computación Numérica Eficiente

Este script demuestra el uso de **NumPy** para el procesamiento eficiente de grandes volúmenes de datos numéricos mediante el uso de arreglos multidimensionales (`ndarrays`).

### Conceptos Aplicados:
*   Creación y manipulación de vectores y matrices ( `array(), arange(), rng.integers(), zeros(), ones()` ).
*   Funciones básicas e informativas ( `type(), size, sum(), min(), max(), std(), mean(), median()` )
*   Operaciones matemáticas (sumas, multiplicación, raíz cuadrada, elevar al cuadrado)
*   Manipulación de estructuras ( `shape, reshape()` )
*   Uniones de estructuras ( `concatenate(), vstack(), hstack()` )
*   Operaciones vectorizadas (evitando bucles `for` ineficientes).
*   Indexación avanzada y máscaras booleanas.

### Cómo ejecutarlo:
```bash
python3 01_numpy_demo/practicas_numpy_usos_basicos.py
```

### Output:

```
### Creación de un array y uso de funciones básicas con NumPy
[12  2  9  4  7 14  3]
Tipo:  <class 'numpy.ndarray'>
Tamaño:  7
Suma:  51
Min:  2
Max:  14
Desviación Estandar:  4.266624149448023
Promedio:  7.285714285714286
Mediana:  7.0
Filtrando menor o iguales que 9:  5

### Creación de secuencia de números, matrices con ceros/unos, operaciones matemáticas
secuencia (inicio, fin, paso)
[ 3  5  7  9 11 13]
aleatorios
[18 27 29 15 12]
matrices con ceros 3x3
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
matrices con unos 3x3
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
operaciones matemáticas (suma 1 a 1)
[5 7 9]
multiplicación por un escalar (1,618 * array)
[6.472 8.09  9.708]
raíz cuadrada
[2.         2.23606798 2.44948974]
elevar al cuadrado
[1 4 9]

### Manipulación de estructuras de datos (shape, reshape)
[ 0  1  2  3  4  5  6  7  8  9 10 11]
(12,)
<class 'numpy.ndarray'>
[[ 0  1  2  3  4  5  6  7  8  9 10 11]]
<class 'numpy.ndarray'>
(1, 12)
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
(2, 6)
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
(3, 4)

### Concatenación de matrices: unión (vstack y hstack)
[4 5 6 1 2 3]
[[11 12 13]
 [14 15 16]
 [17 18 19]]
[[21 22 23]
 [24 25 26]
 [27 28 29]]
unión vetical
[[11 12 13]
 [14 15 16]
 [17 18 19]
 [21 22 23]
 [24 25 26]
 [27 28 29]]
unión horizontal
[[11 12 13 21 22 23]
 [14 15 16 24 25 26]
 [17 18 19 27 28 29]]
equivalencias vstack y hstack
[[11 12 13]
 [14 15 16]
 [17 18 19]
 [21 22 23]
 [24 25 26]
 [27 28 29]]
[[11 12 13 21 22 23]
 [14 15 16 24 25 26]
 [17 18 19 27 28 29]]

### Indexación y filtrado
acceso a 1 elemento
2
sustituir datos
[1 0 3 0]
producto escalar
32
transponer (cambiar filas por columnas)
[[1 2]
 [3 4]]
[[1 3]
 [2 4]]
filtrado (if-else)
['Adol' 'Niño' 'Niño' 'Niño' 'Niño' 'Adol' 'Niño']
<class 'numpy.ndarray'>
filtrado (limpieza valores atipicos. Ej: precios negativos)
[10 35  9  0  3]
filtrado (obtener indices sin cambiar valores)
(array([1, 3]),)
clasificar valores según condición
['espec' 'aprobado' 'espec' 'aprobado' 'espec' 'espec']
filtrado en matrices (actualizar valor según condición)
[[1 8]
 [4 9]]
[[1. 4.]
 [2. 9.]]

### slicing basico [inicio:fin:paso]
[[10 20 30]
 [25 75 15]
 [70 80 90]]
segunda fil
[25 75 15]
<class 'numpy.ndarray'>
tercera col
[30 15 90]
sub matriz filas 0,1 y col 1,2
[[20 30]
 [75 15]]
filas alternas
[[10 20 30]
 [70 80 90]]
filas especificas
[[10 20 30]
 [70 80 90]]
elementos dispersos
[30 80]

### Más filtrados y modificaciones
elementos mayores a un valor. Ej: 75
máscara booleana
[[False False False]
 [False False False]
 [False  True  True]]
elementos filtrados
[80 90]
modificar múltiplos de 20
[[ 10 999  30]
 [ 25  75  15]
 [ 70 999  90]]
invertir orden de filas
[[ 70 999  90]
 [ 25  75  15]
 [ 10 999  30]]
invertir orden de cols
[[ 30 999  10]
 [ 15  75  25]
 [ 90 999  70]]

### Indexación negativa [inicio:fin:paso]
última fila
[ 70 999  90]
penúltima columna
[999  75 999]
últimas dos filas
[[ 25  75  15]
 [ 70 999  90]]
```
