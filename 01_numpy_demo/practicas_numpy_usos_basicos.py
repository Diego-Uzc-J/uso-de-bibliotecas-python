"""
Prácticas con NumPy:
Uso de funciones básicas de la biblioteca NumPy

Ing. Diego A. Uzcátegui J.
diego.uzc [at] gmail.com
Jun 2026

"""

import numpy as np

#creando un array
print('### Creación de un array y uso de funciones básicas con NumPy')
arr = np.array([12,2,9,4,7,14,3])
print(arr)
print('Tipo: ', type(arr))
print('Tamaño: ', arr.size)
print('Suma: ', sum(arr))
print('Min: ', min(arr))
print('Max: ', max(arr))
print('Desviación Estandar: ', arr.std())
print('Promedio: ', np.mean(arr))
print('Mediana: ', np.median(arr))
print('Filtrando menor o iguales que 9: ', ((arr>1)&(arr<=9)).sum()) # 5
print('')


#creando secuencia de numeros
print('### Creación de secuencia de números, matrices con ceros/unos, operaciones matemáticas')
#numeros de 3 al 15, de dos en dos
print('secuencia (inicio, fin, paso)')
arr = np.arange(3, 15, 2)
print(arr)

#5 numeros aleatorios
print('aleatorios')
rng = np.random.default_rng(9)
cinco_enteros = rng.integers(10, 30, size=5)
print(cinco_enteros)

#crear matriz de ceros
print('matrices con ceros 3x3')
matriz = np.zeros((3,3))
print(matriz)

#crear matriz de unos
print('matrices con unos 3x3')
matriz = np.ones((3,3))
print(matriz)

#operaciones matematicas
print('operaciones matemáticas (suma 1 a 1)')# suma( operacion 1 a 1)
a = np.array([1,2,3])
b = np.array([4,5,6])
suma = a + b
print(suma)
print('multiplicación por un escalar (1,618 * array)')
multiplicacion = 1.618 * b
print(multiplicacion)
print('raíz cuadrada')
resultado_raiz = np.sqrt(b) 
print(resultado_raiz)
print('elevar al cuadrado')
resultado_exp = a ** 2 
print(resultado_exp)
print('')

# manipulación de estructuras de datos
print('### Manipulación de estructuras de datos (shape, reshape)')
datos = np.arange(12)
print(datos)
print(datos.shape)
print(type(datos))
#salida (12,) (por omisión)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
# <class 'numpy.ndarray'>

#colocar en 1 filas y 12 col
matriz = datos.reshape(1,12)
print(matriz)
print(type(matriz))
print(matriz.shape)
# [[ 0  1  2  3  4  5  6  7  8  9 10 11]]
# (1, 12)

#colocar en 2 filas y 6 col
matriz = datos.reshape(2,6)
print(matriz)
# ~ [[ 0  1  2  3  4  5]
 # ~ [ 6  7  8  9 10 11]]
print(matriz.shape)

#colocar en 3 filas y 4 col
matriz = datos.reshape(3,4)
print(matriz)
# ~ [[ 0  1  2  3]
 # ~ [ 4  5  6  7]
 # ~ [ 8  9 10 11]]

print(matriz.shape)
# ~ (3, 4)
print('')


# concatenaciones de matrices
print('### Concatenación de matrices: unión (vstack y hstack)')
#concatenar: unir arreglos
union = np.concatenate( (b, a) )
print(union)

matriz_a = np.array([
  [11, 12, 13],
  [14, 15, 16],
  [17, 18, 19]
])
matriz_b = np.array([
  [21, 22, 23],
  [24, 25, 26],
  [27, 28, 29]
])
print(matriz_a)
print(matriz_b)

print('unión vetical')
vertical = np.concatenate( (matriz_a, matriz_b), axis=0)
print(vertical)

print('unión horizontal')
horizontal = np.concatenate( (matriz_a, matriz_b), axis=1)
print(horizontal)

print('equivalencias vstack y hstack')
resultado_v = np.vstack( (matriz_a, matriz_b) )
print(resultado_v)

resultado_h = np.hstack( (matriz_a, matriz_b) )
print(resultado_h)
print('')


#indexación y filtrado
print('### Indexación y filtrado')
matriz = np.array([[1,2],[3,4]])
elemento = matriz[0,1]
print('acceso a 1 elemento')
print(elemento) # 2

#sustituir datos:
print('sustituir datos')
arr = np.array([1,-2,3,-4])
#convierte en cero valores negativos
resultado = np.where(arr > 0, arr, 0)
print(resultado)
#[1 0 3 0]


#algebra lineal 
#producto escalar
print('producto escalar')
prod = np.dot(a,b)
print(prod)

#transpone matriz: cambia filas por col
print('transponer (cambiar filas por columnas)')
print(matriz)
print(matriz.transpose())

#filtrado:
arr = np.array([12,2,9,4,7,14,3])

#(if-else)
print('filtrado (if-else)')
resultado = np.where(arr >= 10, 'Adol', 'Niño')
print(resultado)
print(type(resultado))
# ~ ['Adol' 'Niño' 'Niño' 'Niño' 'Niño' 'Adol' 'Niño']
# ~ <class 'numpy.ndarray'>

#limpiar datos atipicos, ejemplo precios negativos
print('filtrado (limpieza valores atipicos. Ej: precios negativos)')
precios = np.array([10,35,9,-8,3])
precios_limpios = np.where(precios < 0, 0, precios)
print(precios_limpios)
#[10 35  9  0  3]

#obtener indices sin cambiar valores
print('filtrado (obtener indices sin cambiar valores)')
salarios = np.array([1200,4500,2900,13000])
indices = np.where(salarios > 3000)
print(indices)
# ~ (array([1, 3]),)

#varias condiciones
print('clasificar valores según condición')
calificaciones = np.array([4, 9, 2, 10,2,4])
estatus = np.where( (calificaciones >= 5) & (calificaciones <=10), 'aprobado', 'espec' )
print(estatus)

#filtrado en matrices
print('filtrado en matrices (actualizar valor según condición)')
matriz = np.array([[1,8],[4,9]])
print(matriz)
par_impar = np.where( matriz % 2 == 1, matriz, matriz/2)
#mitad de impares
print(par_impar)
print('')

############################################################
#slicing basico [inicio:fin:paso]
print('### slicing basico [inicio:fin:paso]')

matriz = np.array([
  [10, 20, 30],
  [25, 75, 15],
  [70, 80, 90]
])
print(matriz)
#[fil, col]

#segunda fil
print('segunda fil')
print(matriz[1,:])
print(type(matriz[1,:])) #<class 'numpy.ndarray'>

#tercera col
print('tercera col')
print(matriz[:,2])

#sub matriz filas 0,1 y col 1,2
print('sub matriz filas 0,1 y col 1,2')
print(matriz[0:2,1:3])
# ~ [[20 30]
 # ~ [75 15]]

#filas alternas
print('filas alternas')
print(matriz[::2,:])

#filas especificas
print('filas especificas')
print(matriz[[0,2],:])
# ~ [[10 20 30]
 # ~ [70 80 90]]


#elementos dispersos
print('elementos dispersos')
print(matriz[[0,2],[2,1]])
# ~ [30 80]
print('')


print('### Más filtrados y modificaciones')
#mayores de 75
print('elementos mayores a un valor. Ej: 75')
mask_bool = matriz > 75
print('máscara booleana')
print(mask_bool)
print('elementos filtrados')
print(matriz[ mask_bool ])

#modificar multiplos de 20
print('modificar múltiplos de 20')
matriz[matriz % 20 == 0] = 999
print( matriz )

#invertir orden de filas
print('invertir orden de filas')
print(matriz[::-1, :])

#invertir orden de columnas
print('invertir orden de cols')
print(matriz[:, ::-1])
print('')

############################################################
print('### Indexación negativa [inicio:fin:paso]')

#ultima fila
print('última fila')
print(matriz[-1,:])

#penultima col
print('penúltima columna')
print(matriz[:,-2])

#ultimas dos filas
print('últimas dos filas')
print(matriz[-2:,:])
