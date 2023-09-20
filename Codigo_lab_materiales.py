import numpy as np # la necesitamos para operar con vectores y cargar el txt
import pandas as pd
import matplotlib.pyplot as plt # es necesario para graficar
from sklearn.linear_model import LinearRegression

# Cargamos los datos 

datos = pd.read_excel(r"C:\Users\juanf\Downloads\Datos taller Al.xlsx")

datos['Fuerza (kN)'] = (datos['Fuerza (kN)'] / 0.0000402) * 0.001
datos['Cambio en la Long. (mm)'] = datos['Cambio en la Long. (mm)'] / 50

# Escogemos un intervalo para hallar la pendiente
condicion = datos['Cambio en la Long. (mm)'] <= 0.0342
datos_seleccionados = datos[condicion]

X = datos_seleccionados['Cambio en la Long. (mm)'].values.reshape(-1, 1)  # Variables independientes
y = datos_seleccionados['Fuerza (kN)'].values  # Variable dependiente

# Crea un modelo de regresión lineal
model = LinearRegression()

# Ajusta el modelo a los datos seleccionados
model.fit(X, y)

# La pendiente (coeficiente) se encuentra en model.coef_
modulo_young = model.coef_[0]

# Empezamos a graficar 

fig, ax = plt.subplots()

datos.plot(y='Fuerza (kN)', x='Cambio en la Long. (mm)', ax=ax)

plt.xlabel('Deformación unitaria', fontfamily = "times new roman")
plt.ylabel('Esfuerzo (MPa)', fontfamily = "times new roman")
ax.get_legend().remove()

plt.text(0.015, 50, 'Módulo de Young = {:.2f} MPa'.format(modulo_young), 
         fontfamily = "times new roman")

# Linea para hallar el límite de elasticidad y resilencia
x = np.arange(0, 0.05, 0.05/601)
y = modulo_young*(x - 0.002)
linea = pd.DataFrame()
linea['X'] = x
linea['Y'] = y

plt.plot(x, y, '--', c='gray')

# Código para encontrar el punto de intersección

# Escogemos un intervalo para hallar la pendiente
condicion = datos['Cambio en la Long. (mm)'] <= 0.05
datos_seleccionados = datos[condicion]

# Cambio de nombres para que las columnas queden etiquetadas igual
datos_seleccionados = datos_seleccionados.rename(columns={'Fuerza (kN)': 'Y'})

# Calcula la diferencia absoluta entre los valores de las dos columnas en cada fila
diff = datos_seleccionados.sub(linea).abs()

# Encuentra la fila con la distancia total mínima
fila_mas_cercana = diff['Y'].idxmin()

# Grafica del segundo punto mas cercano
coord_x = datos_seleccionados.loc[fila_mas_cercana, 'Cambio en la Long. (mm)']
coord_y = datos_seleccionados.loc[fila_mas_cercana, 'Y']

ax.scatter(coord_x, coord_y, c='red', zorder=5)

plt.text(coord_x + 0.002, coord_y - 12, 'Límite de elasticidad = ({:.2f}, {:.2f})'.format(coord_x, coord_y), 
         fontfamily = "times new roman")

# Area bajo la curva
# Escogemos un intervalo con el límite de elasticidad

condicion = datos['Cambio en la Long. (mm)'] <= coord_x
datos_seleccionados = datos[condicion]
plt.fill_between(datos_seleccionados['Cambio en la Long. (mm)'], 
                 datos_seleccionados['Fuerza (kN)'], color='aquamarine')

area = np.trapz(datos_seleccionados['Cambio en la Long. (mm)'], 
                datos_seleccionados['Fuerza (kN)'])

plt.text(0.015, 36, 'Resilencia = {:.2f} MJ / m{}'.format(area, chr(0xB0 + 3)), 
         fontfamily = "times new roman")

# Límite de ruptura
ax.scatter(datos.tail(1)["Cambio en la Long. (mm)"], datos.tail(1)["Fuerza (kN)"], c='red', zorder=5)

# Resistencia a la tracción
id_resistencia = datos["Fuerza (kN)"].idxmax()
punto_resistencia = datos.iloc(id_resistencia)
print(punto_resistencia)
ax.scatter(datos.tail(1)["Cambio en la Long. (mm)"], datos.tail(1)["Fuerza (kN)"], c='red', zorder=5)

# Guardar la imagen
plt.savefig("Grafica2.jpg", dpi=1200)

# Configuraciones de la graficacion
plt.xticks(np.arange(0.002, 0.200, step=0.01), rotation=45)
plt.show()