import pymongo
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import cv2
import os


class Sistema:

    def __init__(self, client):
        # Creación de la colección y subcolección
        mydb = client["Hospital"]
        self.__data = mydb["Neurología"]

    def obtenerDireccion(self, name: str):
        ruta_archivo = os.path.join(os.getcwd(), name)
        return str(ruta_archivo)

    def asignarData(self, **Data):
        # Data va a ser unas kwargs
        # Busco que este método sea lo más genérico posible
        self.__data.insert_one(Data)


class Imagen:
    def __init__(self, Senal: str):
        self._matcontents = sio.loadmat(Senal)
        self.senal = self._matcontents['data']
        self.sensores = self.senal.shape[0]
        self.puntos = self.senal.shape[1]
        self.epocas = self.senal.shape[2]
        self.senalcontinua = np.reshape(self.senal, (self.sensores, self.puntos * self.epocas), order='F')

    # 1. Imprimir el tamaño de la señal
    def tamaño(self):
        dim = self.senal.ndim
        print('La señal tiene:',
              f'\nDimensión: {dim}',
              f'\nSensores: {self.sensores}',
              f'\nPuntos por época: {self.puntos}',
              f'\nÉpocas: {self.epocas}')

    # 2. Graficar una señal de EEG continua
    def graficarContinua(self, sensor: int):

        # La siguiente gráfica está subdividida en 5 secciones
        # para facilitar su lectura
        fig, ax = plt.subplots(nrows=5, sharex=True, figsize=(12, 6))

        # Número de puntos total en el eje x
        longitud_eje_x = self.puntos * self.epocas

        # Coordenadas de las lineas que subdividen las épocas en la gráfica continua
        coords = np.arange(0, longitud_eje_x, self.puntos, dtype=int)

        for n in range(5):
            ax[n].plot(self.senalcontinua[sensor - 1,
                       int(longitud_eje_x * (n / 5)):
                       int(longitud_eje_x * (n + 1) / 5)],
                       linewidth=0.2, color='k')

            # Lineas que subdividen la gráfica por épocas
            for coord in coords[int(self.epocas * (n / 5)): int(self.epocas * (n + 1) / 5) + 1]:
                # La linea y el texto está ubicada
                # en la coordena de la continua - la longitud de los subplots anteriores
                ax[n].axvline(x=coord - longitud_eje_x * (n / 5),
                              color='blue', linestyle='--')

                ax[n].text(coord - longitud_eje_x * (n / 5) + 400, 8,
                           f'{np.where(coord == coords)[0][0] + 1}',
                           fontsize=6, fontweight='bold')

        ax[0].set_title(f'EEG, Sensor {sensor}', fontsize=16, fontweight='bold')
        ax[2].set_ylabel('Amplitud')
        ax[4].set_xlabel('Puntos')
        plt.show()

    # 3. y 4. Graficar una época de una señal de EEG
    def graficarEpoca(self, epoca: int, sensor: int, color: str = 'k'):

        plt.plot(self.senal[sensor - 1][:][epoca - 1], color=color)

        plt.title(f'Época {epoca}, Sensor {sensor}', fontdict={'fontsize': 16, 'fontweight': 'bold'})
        plt.xlabel('Puntos')
        plt.savefig("signal.png")
        plt.show()

    # 5. Análisis de los datos

    # 5.1. Ver el promedio de las 8 filas de la señal continua

    def promedioTabla(self):
        """Crea una tabla con los promedios de amplitud de cada uno de los sensores"""
        prom_dict = {}
        Sensor= []
        Prom = []        
        for s in range(self.sensores):
            Sensor.append(s + 1)
            Prom.append(np.mean(self.senalcontinua[s]))        
        prom_dict['Sensor'] = Sensor
        prom_dict['Promedio de Amplitud'] = Prom        
        return pd.DataFrame(prom_dict, columns=['Sensor', 'Promedio de Amplitud'])

    # 5.2. Ver el histograma del promedio del punto 1 
    def promedioGrafica(self):
        sns.barplot(data=self.promedioTabla, x='Sensor', y='Promedio de Amplitud')
        plt.show()

    # 5.3. Ver una imagen de calor (sns.heatmap) con colores llamativos, tome las 100
    # primeras muestras y las 100 ultimas de la señal por épocas para ingresar a la función 
    # una arreglo de (100,100) y guarde la imagen
    def mapaCalor(self):
        map = self.senal[0, :100, :-100]
        sns.heatmap(map, cmap="viridis")
        plt.savefig("hmcolor.png")
        plt.show()

    # 5.4. Muestre en una ventana llamada “Heatmap” donde se vea la imagen en blanco y 
    # negro y guarde la imagen
    def mapaCalorB(self):
        imagen = cv2.imread('hmcolor.png')
        img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Heatmap', img_gris)
        cv2.imwrite('hmBN.png', img_gris)
        cv2.waitKey(0)


def intput(msg=''):
    try:
        valor_numerico = int(input(msg))
        return valor_numerico
    except ValueError:
        print("Por favor ingresar solo números.")
        return intput(msg)


def sensor_input(imagen):
    sensor = intput(f'''
            Ingrese el sensor.
            Los sensores disponibles estan entre 1 y {imagen.sensores}
            > ''')
    if 0 < sensor <= imagen.sensores:
        return sensor
    else:
        print('Opción inválida, intente nuevamente')
        return sensor_input(imagen)


def epoca_input(imagen):
    epoca = intput(f'''
            Ingrese la época
            Las épocas disponibles estan entre 1 y {imagen.epocas}
            > ''')
    if 0 < epoca <= imagen.epocas:
        return epoca
    else:
        print('Opción inválida, intente nuevamente')
        return epoca_input(imagen)


def main():
    # Creamos el servidor
    client = pymongo.MongoClient(
        "mongodb+srv://jjosecortes:jjosecortes@info2.1k5lrgf.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    paciente = Sistema(client)

    cedula = intput('Ingresar su número de cédula: ')
    nombre = input('Ingrese su nombre: ')
    edad = intput('Ingrese su edad: ')

    print('\nSISTEMA LECTURA DE SEÑALES')

    # Creamos la imagen
    Senal = input('Introduzca la ruta de la señal: ')
    imagen = Imagen(Senal)

    while True:
        op = intput('''
        MENÚ 1
        1. Ver tamaño de la señal
        2. Graficar una señal de EEG continua
        3. Graficar una época de señal de EEG
        4. Graficar un color determinado
        5. Análisis de los datos
        6. Guardar información y Salir 
        >> ''')

        if op == 1:
            imagen.tamaño()

        elif op == 2:
            sensor = sensor_input(imagen)
            imagen.graficarContinua(sensor=sensor)

        elif op == 3:
            sensor = sensor_input(imagen)
            epoca = epoca_input(imagen)
            imagen.graficarEpoca(epoca=epoca, sensor=sensor)

        elif op == 4:
            # Este try verifica que ya hallan sido ingresados sensor y época
            try:
                color = input(f'''
            Ingrese el color que desea aplicar a la señal en formato hexadecimal:  ''')

                # Este try verifica que el color sea válido
                try:
                    imagen.graficarEpoca(epoca=epoca, sensor=sensor, color=color)

                except ValueError:
                    print('El color ingresado no es válido')

            except UnboundLocalError:
                sensor = sensor_input(imagen)
                epoca = epoca_input(imagen)

                # Este try verifica que el color sea válido
                try:
                    imagen.graficarEpoca(epoca=epoca, sensor=sensor, color=color)

                except ValueError:
                    print('El color ingresado no es válido')

        elif op == 5:
            while True:
                op2 = intput('''
        MENÚ 2
        1. Ver el promedio de las 8 filas de la señal continua
        2. Ver el histograma del promedio del punto 1
        3. Ver una imagen de calor
        4. Imagen en blaco y negro
        5. Regresar
        >> ''')

                if op2 == 1:
                    print('\n')
                    print(imagen.promedioTabla.to_string(index=False))

                elif op2 == 2:
                    imagen.promedioGrafica()

                elif op2 == 3:
                    imagen.mapaCalor()

                elif op2 == 4:
                    imagen.mapaCalorB()

                elif op2 == 5:
                    break

                else:
                    print('Opción Inválida, intente nuevamente.')

        elif op == 6:
            paciente.asignarData(Cedula=cedula,
                                 Nombre=nombre,
                                 Edad=edad,
                                 Señal=Senal,
                                 Imagen_Señal=Sistema(client).obtenerDireccion('signal.png'),
                                 Mapa_de_calor=Sistema(client).obtenerDireccion('hmcolor.png'))
            print('Fin del programa...')
            break

        else:
            print('Opción Inválida, intente nuevamente.')


if __name__ == '__main__':
    main()
