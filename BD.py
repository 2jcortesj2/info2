class Persona:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
    
    def asignarNombre(self, nombre):
        self.__nombre = nombre
    
    def asignarCedula(self, Cedula):
        self.__cedula = Cedula

    def asignarGenero(self, Genero):
        self.__genero = Genero
    
    def verNombre(self):
        return self.__nombre
    
    def verCedula(self):
        return self.__cedula
    
    def verGenero(self):
        return self.__genero

class Paciente:
    def __init__(self):
        self.__servicio = ""

    def asignarServicio(self, servicio):
        self.__servicio = servicio

    def verServicio(self):
        return self.__servicio
    
class Empleado(Persona):
    def __init__(self):
        self.__turno = ""
    def asignarTurno(self, turno):
        self.__turno = turno
    def verTurno(self, turno):
        return self.__turno

class Enfermera(Empleado):
    def __init__(self):
        self.__rango = ""
    def asignarRango(self, rango):
        self.__rango = rango
    def verRango(self):
        return self.__rango

class Medico(Empleado):
    def __init__(self):
        self.__especialidad = ""
    def asignarEspecialidad(self, especialidad):
        self.__especialidad = especialidad
    def verEspecialidad(self):
        return self.__especialidad