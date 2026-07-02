"""
Prácticas con NumPy:
Uso de funciones básicas de la biblioteca NumPy

Ing. Diego A. Uzcátegui J.
diego.uzc [at] gmail.com
Jun 2026

"""

import pandas as pd

print('### Creación de un DataFrame (df) desde un diccionario con Pandas')
datos_usuarios = {'nombre': ['Juana', 'Pedro', 'Simón', 'Romulo'], 'edad': [26, 19, 23, 35], 'rol': ['vendedor', 'técnico', 'vendedor', 'secretario']}
df1 = pd.DataFrame(datos_usuarios)
print(type(df1))
#<class 'pandas.core.frame.DataFrame'>

print('guardar datos en csv')
df1.to_csv('02_pandas_demo/usuarios_escribir.csv', index=False)

print('leer desde csv') # para archivos excel utilizar read_excel()
df2 = pd.read_csv('02_pandas_demo/usuarios_lectura.csv')
print(df2)

print('### Explorar y resumir')
print('head(n) : primeros n registros')
print(df1.head(2))
print('info() : tipo, cantidad de registros, cantidad de col, tipos de datos, memoria')
print(df1.info())
print('describe(): count, media, desviación estandar (std), min, max, cuartiles')
print(df1.describe())

print('### Unir DataFrames')
print('join() : equivalente apilado horizontal')
df_unido = df1.join(df2, lsuffix='_df1', rsuffix='_df2')
print(df_unido)

print('merge() : unir por col clave (manteniendo col que coinciden en ambas)')
df_unido = df1.merge(df1, on='nombre', how='inner')
print(df_unido)

print('merge() : unir por col clave (todas las filas de df1 y rellenando NaN donde no hay en df2)')
df_unido = df1.merge(df1, on='nombre', how='left')
print(df_unido)


print('apilar concat (horizontal axis=1)')
df_apilado = pd.concat([df1,df2], axis=1)
print(df_apilado)

print('apilar concat (vertical axis=0)')
df_apilado = pd.concat([df1,df2], axis=0)
print(df_apilado)
#elimnar duplicados
print('luego de eliminar duplicados')
df_sin_dup = df_apilado.drop_duplicates(subset=['nombre'], keep='first')
df_a = df_sin_dup.reset_index(drop=True)
print(df_sin_dup)


print('### Selección y filtrado de DataFrames')
print(type(df_a)) # <class 'pandas.core.frame.DataFrame'>
print('seleccionando 1 col')
print(df_a['nombre'])
print(type(df_a['nombre'])) # simle[[corchetes]] => <class 'pandas.core.series.Series'>
print(type(df_a[['nombre']])) # doble[[corchetes]] => <class 'pandas.core.frame.DataFrame'>

print('seleccionando 2 col')
print(df_a[['nombre', 'rol']])
print(type(df_a[['nombre', 'rol']])) # <class 'pandas.core.frame.DataFrame'>

#mask
print('filtra filas por condición: genera una Serie dtype: bool (también conocida como máscara boleana)')
serie_bool = df_a['edad'] > 25
print(df_a['edad'] > 25)
print(type(df_a['edad'] > 25)) # <class 'pandas.core.series.Series'>
print(df_a[serie_bool]) # equivalente a df_a[ df_a['edad'] > 25 ] <- devuelve DataFrame
print(type(df_a[serie_bool])) # <class 'pandas.core.frame.DataFrame'>

print('seleccionar con loc (etiquetas), iloc (índice numérico)')
print(df_a.loc[3, 'rol']) # secretario
print(df_a.iloc[4, 2]) #cajero


print('### Manipulación y limpieza de datos')
print('eliminar filas con un valor nulo')
print(df_a.dropna())

print('rellenar valores nulos')
df_a['edad'] = df_a['edad'].fillna(0)
print(df_a)
print('eliminar fila especifica')
print(df_a.drop([4]))
print(df_a)
print('ordenar por columna')
print( df_a.sort_values(by='edad') )
#print(df_a)

print('### Agrupamiento de datos')
promedio_edad = df_a.groupby('rol')['edad'].mean()
print(promedio_edad)
cantidad = df_a.groupby('rol')['edad'].count()
print(cantidad)
