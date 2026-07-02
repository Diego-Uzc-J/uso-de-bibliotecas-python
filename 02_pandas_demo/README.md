# Demostración de Pandas: Análisis de DataFrames

Este proyecto implementa **Pandas** para simular un flujo de trabajo real de análisis de datos: desde la carga de un archivo hasta la obtención de métricas clave.

### Conceptos Aplicados:
*   Carga y lectura de archivos (CSV / Excel) ( `read_csv()/read_excel()` ).
*   Guardar datos en CSV ( `to_csv()` )
*   Funciones informativas y estadísticas descriptivas ( `info(), head(), describe()` )
*   Unión de DataFrames horizontal y vertical ( `join(), merge(), concat()` ). 
*   Selección de datos y filtrado ( `loc(), iloc()`, condiciones de filtrado ).
*   Tratamiento de valores nulos o faltantes, o duplicados ( `drop_duplicates(), dropna(), fillna()` ).
*   Ordenamiento por columnas ( `sort_values()` ).
*   Filtrado de datos bajo múltiples condiciones.
*   Agrupación de datos ( `groupby()` ).

### Cómo ejecutarlo:
```bash
python3 02_pandas_demo/practicas_pandas_usos_basicos.py
```
### Output:
```
### Creación de un DataFrame (df) desde un diccionario con Pandas
<class 'pandas.core.frame.DataFrame'>
guardar datos en csv
leer desde csv
      nombre  edad            rol
0     Miguel  32.0         cajero
1     Samuel  17.0    programador
2  Elizabeth  24.0       vendedor
3      Pedro  21.0        tecnico
4      Felix   NaN         cajero
5    Mariano   4.0  recepcionista
### Explorar y resumir
head(n) : primeros n registros
  nombre  edad       rol
0  Juana    26  vendedor
1  Pedro    19   técnico
info() : tipo, cantidad de registros, cantidad de col, tipos de datos, memoria
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   nombre  4 non-null      object
 1   edad    4 non-null      int64 
 2   rol     4 non-null      object
dtypes: int64(1), object(2)
memory usage: 228.0+ bytes
None
describe(): count, media, desviación estandar (std), min, max, cuartiles
            edad
count   4.000000
mean   25.750000
std     6.800735
min    19.000000
25%    22.000000
50%    24.500000
75%    28.250000
max    35.000000
### Unir DataFrames
join() : equivalente apilado horizontal
  nombre_df1  edad_df1     rol_df1 nombre_df2  edad_df2      rol_df2
0      Juana        26    vendedor     Miguel      32.0       cajero
1      Pedro        19     técnico     Samuel      17.0  programador
2      Simón        23    vendedor  Elizabeth      24.0     vendedor
3     Romulo        35  secretario      Pedro      21.0      tecnico
merge() : unir por col clave (manteniendo col que coinciden en ambas)
   nombre  edad_x       rol_x  edad_y       rol_y
0   Juana      26    vendedor      26    vendedor
1   Pedro      19     técnico      19     técnico
2   Simón      23    vendedor      23    vendedor
3  Romulo      35  secretario      35  secretario
merge() : unir por col clave (todas las filas de df1 y rellenando NaN donde no hay en df2)
   nombre  edad_x       rol_x  edad_y       rol_y
0   Juana      26    vendedor      26    vendedor
1   Pedro      19     técnico      19     técnico
2   Simón      23    vendedor      23    vendedor
3  Romulo      35  secretario      35  secretario
apilar concat (horizontal axis=1)
   nombre  edad         rol     nombre  edad            rol
0   Juana  26.0    vendedor     Miguel  32.0         cajero
1   Pedro  19.0     técnico     Samuel  17.0    programador
2   Simón  23.0    vendedor  Elizabeth  24.0       vendedor
3  Romulo  35.0  secretario      Pedro  21.0        tecnico
4     NaN   NaN         NaN      Felix   NaN         cajero
5     NaN   NaN         NaN    Mariano   4.0  recepcionista
apilar concat (vertical axis=0)
      nombre  edad            rol
0      Juana  26.0       vendedor
1      Pedro  19.0        técnico
2      Simón  23.0       vendedor
3     Romulo  35.0     secretario
0     Miguel  32.0         cajero
1     Samuel  17.0    programador
2  Elizabeth  24.0       vendedor
3      Pedro  21.0        tecnico
4      Felix   NaN         cajero
5    Mariano   4.0  recepcionista
luego de eliminar duplicados
      nombre  edad            rol
0      Juana  26.0       vendedor
1      Pedro  19.0        técnico
2      Simón  23.0       vendedor
3     Romulo  35.0     secretario
0     Miguel  32.0         cajero
1     Samuel  17.0    programador
2  Elizabeth  24.0       vendedor
4      Felix   NaN         cajero
5    Mariano   4.0  recepcionista
### Selección y filtrado de DataFrames
<class 'pandas.core.frame.DataFrame'>
seleccionando 1 col
0        Juana
1        Pedro
2        Simón
3       Romulo
4       Miguel
5       Samuel
6    Elizabeth
7        Felix
8      Mariano
Name: nombre, dtype: object
<class 'pandas.core.series.Series'>
<class 'pandas.core.frame.DataFrame'>
seleccionando 2 col
      nombre            rol
0      Juana       vendedor
1      Pedro        técnico
2      Simón       vendedor
3     Romulo     secretario
4     Miguel         cajero
5     Samuel    programador
6  Elizabeth       vendedor
7      Felix         cajero
8    Mariano  recepcionista
<class 'pandas.core.frame.DataFrame'>
filtra filas por condición: genera una Serie dtype: bool (también conocida como máscara boleana)
0     True
1    False
2    False
3     True
4     True
5    False
6    False
7    False
8    False
Name: edad, dtype: bool
<class 'pandas.core.series.Series'>
   nombre  edad         rol
0   Juana  26.0    vendedor
3  Romulo  35.0  secretario
4  Miguel  32.0      cajero
<class 'pandas.core.frame.DataFrame'>
seleccionar con loc (etiquetas), iloc (índice numérico)
secretario
cajero
### Manipulación y limpieza de datos
eliminar filas con un valor nulo
      nombre  edad            rol
0      Juana  26.0       vendedor
1      Pedro  19.0        técnico
2      Simón  23.0       vendedor
3     Romulo  35.0     secretario
4     Miguel  32.0         cajero
5     Samuel  17.0    programador
6  Elizabeth  24.0       vendedor
8    Mariano   4.0  recepcionista
rellenar valores nulos
      nombre  edad            rol
0      Juana  26.0       vendedor
1      Pedro  19.0        técnico
2      Simón  23.0       vendedor
3     Romulo  35.0     secretario
4     Miguel  32.0         cajero
5     Samuel  17.0    programador
6  Elizabeth  24.0       vendedor
7      Felix   0.0         cajero
8    Mariano   4.0  recepcionista
eliminar fila especifica
      nombre  edad            rol
0      Juana  26.0       vendedor
1      Pedro  19.0        técnico
2      Simón  23.0       vendedor
3     Romulo  35.0     secretario
5     Samuel  17.0    programador
6  Elizabeth  24.0       vendedor
7      Felix   0.0         cajero
8    Mariano   4.0  recepcionista
      nombre  edad            rol
0      Juana  26.0       vendedor
1      Pedro  19.0        técnico
2      Simón  23.0       vendedor
3     Romulo  35.0     secretario
4     Miguel  32.0         cajero
5     Samuel  17.0    programador
6  Elizabeth  24.0       vendedor
7      Felix   0.0         cajero
8    Mariano   4.0  recepcionista
ordenar por columna
      nombre  edad            rol
7      Felix   0.0         cajero
8    Mariano   4.0  recepcionista
5     Samuel  17.0    programador
1      Pedro  19.0        técnico
2      Simón  23.0       vendedor
6  Elizabeth  24.0       vendedor
0      Juana  26.0       vendedor
4     Miguel  32.0         cajero
3     Romulo  35.0     secretario
### Agrupamiento de datos
rol
cajero           16.000000
programador      17.000000
recepcionista     4.000000
secretario       35.000000
técnico          19.000000
vendedor         24.333333
Name: edad, dtype: float64
rol
cajero           2
programador      1
recepcionista    1
secretario       1
técnico          1
vendedor         3
Name: edad, dtype: int64
```
