import numpy as np # la necesitamos para operar con vectores y cargar el txt
import pandas as pd
import matplotlib.pyplot as plt # es necesario para graficar
from sklearn.linear_model import LinearRegression

# Cargamos los datos 

datos = pd.read_csv("Acero bajo carbono.txt", delimiter="\t").astype(float)

datos['Fuerza'] = (datos['Fuerza'] / 0.0000149) * 1e-6
datos['Desplazamiento'] = datos['Desplazamiento'] / 50

# Escogemos un intervalo para hallar la pendiente
condicion = datos['Desplazamiento'] <= 0.092
datos_seleccionados = datos[condicion]

X = datos_seleccionados['Desplazamiento'].values.reshape(-1, 1)  # Variables independientes
y = datos_seleccionados['Fuerza'].values  # Variable dependiente

# Crea un modelo de regresión lineal
model = LinearRegression()

# Ajusta el modelo a los datos seleccionados
model.fit(X, y)

# La pendiente (coeficiente) se encuentra en model.coef_
modulo_young = model.coef_[0]

# Empezamos a graficar 

fig, ax = plt.subplots()

datos.plot(y='Fuerza', x='Desplazamiento', ax=ax)

plt.xlabel('Deformación unitaria', fontfamily = "times new roman")
plt.ylabel('Esfuerzo (MPa)', fontfamily = "times new roman")
ax.get_legend().remove()

plt.text(0.015, 50, 'Módulo de Young = {:.2f} MPa'.format(modulo_young), 
         fontfamily = "times new roman")

# Linea para hallar el límite de elasticidad y resilencia
x = np.arange(0, 0.15, 0.15/7508)
y = modulo_young*(x - 0.002)
linea = pd.DataFrame()
linea['X'] = x
linea['Y'] = y

plt.plot(x, y, '--', c='gray')

# Código para encontrar el punto de intersección

# Escogemos un intervalo para hallar la resilencia
condicion = datos['Desplazamiento'] <= 0.15
datos_seleccionados = datos[condicion]

# Cambio de nombres para que las columnas queden etiquetadas igual
datos_seleccionados = datos_seleccionados.rename(columns={'Fuerza': 'Y'})

# Calcula la diferencia absoluta entre los valores de las dos columnas en cada fila
diff = datos_seleccionados.sub(linea).abs()

# Encuentra la fila con la distancia total mínima
fila_mas_cercana = diff['Y'].idxmin()

# Grafica del segundo punto mas cercano
coord_x = datos_seleccionados.loc[fila_mas_cercana, 'Desplazamiento']
coord_y = datos_seleccionados.loc[fila_mas_cercana, 'Y']

ax.scatter(coord_x, coord_y, c='red', zorder=5)

plt.text(coord_x + 0.002, coord_y - 240, 'Límite de elasticidad = {:.2f} MPa'.format(coord_y), 
         fontfamily = "times new roman")

# Area bajo la curva
# Escogemos un intervalo con el límite de elasticidad

condicion = datos['Desplazamiento'] <= coord_x
datos_seleccionados = datos[condicion]
plt.fill_between(datos_seleccionados['Desplazamiento'], 
                 datos_seleccionados['Fuerza'], color='aquamarine')

print(coord_x * coord_y / 2)

area = np.trapz(datos_seleccionados['Desplazamiento'], 
                datos_seleccionados['Fuerza'])

plt.text(0.015, 300, 'Resilencia = {:.2f} MJ / m{}'.format(area, chr(0xB0 + 3)), 
         fontfamily = "times new roman")

# Límite de ruptura
coord_x = datos.tail(1)["Desplazamiento"]
coord_y = datos.tail(1)["Fuerza"]

ax.scatter(coord_x, coord_y, c='red', zorder=5)

plt.text(coord_x - 0.235, coord_y - 300, 'Límite de ruptura = {:.2f} MPa'.format(coord_y.values[0]), 
         fontfamily = "times new roman")

# Resistencia a la tracción
id_resistencia = datos["Fuerza"].idxmax()
punto_resistencia = datos.loc[id_resistencia]

coord_x = punto_resistencia.iloc[2]
coord_y = punto_resistencia.iloc[1]

ax.scatter(coord_x, coord_y, c='red', zorder=5)

plt.text(coord_x - 0.15, coord_y + 100, 'Resistencia a la tracción = {:.2f} MPa'.format(punto_resistencia.iloc[1]), 
         fontfamily = "times new roman")

# Guardar la imagen
plt.savefig("Grafica2.jpg", dpi=1200)

# Configuraciones de la graficacion
plt.title('Ensayo de tracción', fontfamily = "times new roman")
plt.show()