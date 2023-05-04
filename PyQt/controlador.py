# Petición y comunicación entre modelo y vista
from PyQt5 import QtWidgets
import sys

# Modelo
from modelo import Sistema, client

# Vista
from vista import Ventana

class comunicacion(object):
    def __init__ (self):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__view = Ventana()
        self.system = Sistema(client)
        self.controller = ctrl(self.__view, self.system)
        self.__view.conexionconelcontrolador(self.controller)

    def main(self):
        self.__view.show()
        sys.exit(self.__app.exec_())

class ctrl(object):
    def __init__ (self, view, system):
        self.__view = view
        self.system = system

    def agregarpacientes(self, cc, nombre, edad):
        self.system.cedula(cc)
        self.system.nombre(cc, nombre)
        self.system.edad(cc,edad)

    def buscarensistema(self,cc):
        nombre, edad = self.system.verificar_db(cc)
        if nombre != None:
            self.__view.rellenar_datos(nombre, edad)
        else:
            print("El paciente no existe")

if __name__ == "__main__":
    controller = comunicacion()
    controller.main()