# Respuesta grafica

# importamos 1as Librerías necesarias
from PyQt5 import QtWidgets, uic

# Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets. QMainWindow):
    '''Esta es la clase principal'''
    # Inicializanos la ventana y conectanos los botones
    def __init__(self):
        # Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi('Menu.ui', self) # Lee el archivo de QtDesigner
    
    # Conectar botones a funciones
        self.Verificar.clicked.connect(self.verificar_dato)
        self.Agregar.clicked.connect(self.agregar_dato)
        self.Salir.clicked.connect(self.cerrar)
        self.Continuar.setEnabled(False)
        self.Continuar.clicked.connect(self.continuar_dato)

    def conexionconelcontrolador (self, control):
        self.mi_controlador = control

    def verificar_dato(self):
        self.mi_controlador.buscarensistema(self.Ingresecedula.text())

    def rellenar_datos(self,nombre, edad):
        self.Verificar.setEnabled(False)
        self.Ingresenombre.setText(nombre)
        self.Ingreseedad.setText(str(edad))

    def agregar_dato(self):
        self.mi_controlador.agregarpacientes(self.Ingresecedula.text(), self.Ingresenombre.text(), self.Ingreseedad.text())
        self.Agregar.setEnabled(False)
        self.Continuar.setEnabled(True)

    def cerrar(self):
        self.close()

    def continuar_dato(self):
        print("menu_grafica")

