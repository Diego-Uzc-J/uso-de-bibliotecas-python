"""
Prácticas con Matplotlib:
Uso de funciones básicas de la biblioteca Matplotlib, que se utiliza para analisis exploratorio de datos (EDA) y presentación de resultados

Ing. Diego A. Uzcátegui J.
diego.uzc [at] gmail.com
Jun 2026

"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

datos_anhos = [2020,2021,2022,2023,2024,2025,2026]
datos_ventas1 = [27,28,31,33,36,42,45]
datos_ventas2 = [25,28,32,36,39,41,45]
datos_ventas3 = [25,27,31,38,43,43,45]

# --- Figura 1 ---------------------------------------------------------
print('### Gráficos de lineas plt.plot(). series temporales, datos continuos. Ej: crecimiento de ventas.')
line1, = plt.plot(datos_anhos, datos_ventas1, marker='o', color='b', linestyle='solid')
line2, = plt.plot(datos_anhos, datos_ventas2, marker='s', color='g', linestyle='dashdot')
line3, = plt.plot(datos_anhos, datos_ventas3, marker='D', color='r', linestyle='dotted')
plt.legend([line1, line2, line3], ['Venta Tienda 1', 'Venta Tienda 2', 'Venta Tienda 3'])

plt.title('Gráfico básico con plt.plot()', fontsize=18, fontweight='bold')
plt.xlabel('Años')
plt.ylabel('Venta en $1K')
plt.grid(True)

plt.show()


# --- Figura 2 ---------------------------------------------------------
print('### Diagrama de dispersión plt.scatter(). observar agrupaciones o correlación de dos variables númericas. Ej: estatura y peso.')
# Estatura en metros
estatura = np.array([1.55, 1.58, 1.61, 1.63, 1.65, 1.68, 1.70, 1.72, 1.74, 1.76, 
                     1.78, 1.80, 1.82, 1.84, 1.86, 1.89, 1.91, 1.93, 1.95, 1.98])

# Peso en kilogramos
peso = np.array([54.2, 57.1, 60.5, 62.3, 65.0, 68.4, 71.2, 73.5, 76.1, 78.8, 
                 81.3, 84.5, 87.0, 89.6, 92.4, 95.8, 98.2, 101.5, 104.1, 107.5])

#edades
edad = np.array([21, 35, 19, 44, 28, 52, 23, 31, 48, 60, 
                 25, 39, 42, 55, 30, 27, 46, 33, 50, 62])

plt.scatter(peso, estatura, c=edad, alpha=0.5,cmap='viridis', edgecolors='black')
plt.title('Gráfico de dispersión. plt.scatter()', fontsize=18, fontweight='bold')
plt.xlabel('Peso en Kg')
plt.ylabel('Estatura en metros')

#barra de color
plt.colorbar(label='Edad (años)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


# --- Figura 3 ---------------------------------------------------------
print('### Gráficos de barras plt.bar(). Comparar valores de variables discretas. Ej: Preferencia en Área TI.')
rng = np.random.default_rng(seed=18)
areas = ['Inteligencia Artificial (IA)', 'Ciencia de Datos', 'Ciberseguridad', 'Computación en la Nube', 'Desarrollo de Software' ]
cantidad_usuarios = rng.integers(500, 1000, 5)

#colores = ['red', 'blue', 'green', 'orange', 'skyblue']
colores_pasteles = ['#FFB7B2', '#B5E2FA', '#FFF9B3', '#C1E1C1', '#D1B3E2']

plt.bar(areas, cantidad_usuarios, color=colores_pasteles, edgecolor='black')
plt.title('Cantidad de usuarios por área TI. Gráfico con plt.bar()', fontsize=18, fontweight='bold')
plt.xlabel('Áreas TI', fontsize=12)
plt.ylabel('Cantidad de usuarios', fontsize=12)

plt.show()


# --- Figura 4 ---------------------------------------------------------
print('### Gráficos circular plt.pie(). Mostrar proporción de opciones seleccionadas. Ej: Lenguaje de programación más popular.')
# Top 10 de lenguajes de programación más populares
lenguajes = ['Python', 'C', 'Java', 'C++', 'C#', 'JavaScript', 'SQL', 'PHP', 'TypeScript', 'Rust']
cuotas = [22.61, 11.05, 8.71, 7.39, 6.83, 5.00, 4.50, 3.80, 2.78, 2.34]

colores = ['#3572A5', '#555555', '#b07219', '#f34b7d', '#178600', 
           '#f1e05a', '#e0c3fc', '#4F5D95', '#2b7489', '#dea584']

# Resaltar la opción Python separándola un poco
separacion = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0) 

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    cuotas, 
    labels=lenguajes, 
    explode=separacion, 
    colors=colores, 
    autopct='%1.2f%%',   # Porcentaje con dos decimales
    shadow=True,         # Efecto de sombra
    startangle=120       # Comienza en un ángulo de 120 grados
)

ax.set_title("Top 10 Lenguajes de Programación más Populares (2026)", fontsize=18, fontweight='bold')
ax.axis('equal')  
plt.show()


# --- Figura 5 ---------------------------------------------------------
print('### Histogramas plt.hist(). Distribución de frecuencias en un conjunto de datos númericos. Ej: conjunto de edades.')
#datos con distribución normal
np.random.seed(99)
datos_edades = np.random.normal(loc=22, scale=9, size=512)
datos_edades = datos_edades[datos_edades >= 15]
plt.figure( figsize=(8,5) )

plt.hist(datos_edades, bins=25, color='blue', edgecolor='black', alpha=0.7)

plt.title('Histograma: Edades de Estudiantes de Ingenieria de Sistemas.', fontsize=18, fontweight='bold')
plt.ylabel('Frecuencia')
plt.xlabel('Edades')

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


# --- Figura 6 ---------------------------------------------------------
print('### Diagrama de caja plt.boxplot(). Ideal para identificar valores atípicos, dispersión, asimetría. Ej: Detección de tiempos de carga de aplicación web.')
#resume un conjunto de datos numéricos usando cinco valores clave: el mínimo, el primer cuartil (Q1), la mediana, el tercer cuartil (Q3) y el máximo.
np.random.seed(25)
datos_gr1 = np.random.normal(100, 20, 200)
datos_gr2 = np.random.normal(80, 30, 200)
datos_gr3 = np.random.normal(110, 15, 200)
datos_gr4 = np.random.normal(95, 25, 200)
datos_gr5 = np.random.normal(105, 10, 200)

#agrupa datos en lista
datos_box = [datos_gr1, datos_gr2, datos_gr3, datos_gr4, datos_gr5]

#figura y ejes
fig, ax = plt.subplots(figsize=(8,5))

bp = ax.boxplot(datos_box,
                 patch_artist=True,#rellena las cajas con color
                 tick_labels=['Data Preparation / Preprocessing', 'Modeling', 'Evaluation', 'Deployment', 'Monitoring & Maintenance'],
                 notch=True,#una muesca en la mediana
                 showmeans=True) #media con un marcador

colores = ['lightblue', 'lightgreen', 'lightgrey', '#D1B3E2','#FFB7B2']
for patch, color in zip(bp['boxes'], colores):
    patch.set_facecolor(color)
    
ax.set_title('Diagrama de caja. Gráfico con plt.boxplot()', fontsize=18, fontweight='bold')
ax.set_ylabel('Tiempos de Carga')
ax.set_xlabel('Aplicaciones')

plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# --- Figura 7 ---------------------------------------------------------
print('### Varios diagramas en un figura. Ej: Comparación de áreas TI desde varias perspectivas (linea de tiempo, proporciones, etc).')

# Set de datos estructurado en un DataFrame de Pandas
datos_ti = {
    "Año": [2022, 2023, 2024, 2025, 2026],
    "Inteligencia Artificial": [20, 35, 55, 80, 120],
    "Ciberseguridad": [45, 52, 60, 72, 85],
    "Cloud Computing": [70, 85, 98, 110, 125],
    "Desarrollo de Software": [90, 95, 102, 108, 115],
    "Ciencia de Datos": [30, 40, 52, 68, 88],
}
df = pd.DataFrame(datos_ti)

# variables de apoyo para graficar
areas = df.columns[1:]
años = df["Año"]
valores_actuales = df.iloc[-1, 1:]  # Datos del último año (2026)
colores = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

# 2. Mostraremos 4 gráficos en una cuadrícula de 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 11))

# GRÁFICO 1 (0,0): Barras Verticales (Comparación en el último año) ---
axs[0, 0].bar(areas, valores_actuales, color=colores)
axs[0, 0].set_title("Proporción Actual por Área TI (2026)")
axs[0, 0].set_ylabel("Valor de Mercado (Billones USD)")
axs[0, 0].set_xticks(range(len(areas)))
axs[0, 0].set_xticklabels(areas, rotation=15, ha="right")

# GRÁFICO 2 (0,1): Pastel / Pie (Distribución porcentual en el último año) ---
axs[0, 1].pie(
    valores_actuales,
    labels=areas,
    autopct="%1.2f%%",
    startangle=140,
    colors=colores,
)
axs[0, 1].set_title("Participación de Mercado Total (2026)")

# GRÁFICO 3 (1,0): Barras Horizontales (Crecimiento total acumulado 5 años) ---
# Calculamos la diferencia entre el año final (2026) y el inicial (2022)
crecimiento_total = df.iloc[-1, 1:] - df.iloc[0, 1:]
axs[1, 0].barh(areas, crecimiento_total, color=colores, edgecolor="black")
axs[1, 0].set_title("Crecimiento Neto Acumulado (2022 vs 2026)")
axs[1, 0].set_xlabel("Incremento en Billones USD")

# GRÁFICO 4 (1,1): Crecimiento en el tiempo (Líneas temporales) ---
for i, area in enumerate(areas):
    axs[1, 1].plot(
        años,
        df[area],
        marker="o",
        linewidth=2,
        color=colores[i],
        label=area,
    )
axs[1, 1].set_title("Evolución y Crecimiento Temporal (5 Años)")
axs[1, 1].set_xlabel("Año")
axs[1, 1].set_ylabel("Valor de Mercado (Billones USD)")
axs[1, 1].set_xticks(años)
axs[1, 1].legend(loc="upper left", fontsize="small")

plt.tight_layout()
plt.show()
