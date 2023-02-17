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

class Sistema( Persona ):
    
    def _init_(self):
        self.__lista_pacientes = []
        self.__lista_nombre = []
        self.__lista_cedula = []
        self.__lista_genero = []
        self.__diccionario_pacientes = {  }

    def numeroDePacientes( self ):
        self._numero_pacientes = len( self._lista_pacientes )
        return self.__numero_pacientes
    
    def ingresarPaciente( self, rol ):
        p = Paciente() 
        p.setName( rol )
        p.setGenero( rol )
        p.setCedula( rol )
        p.assignService()
        self.__lista_pacientes.append( p.guardarInfo() )
        self.__lista_nombre.append( p.getName() )
        self.__lista_cedula.append( p.getCedula() )
        self.__lista_genero.append( p.getGenero() )
        self._diccionario_pacientes.update( {'Nombre' : self.lista_nombre, 'Cedula' : self.lista_cedula, 'Genero' : self._lista_genero} )

        print( self.__lista_pacientes )
        print( self.numeroDePacientes() )

    def verDatosPacientesLista( self ):
        cedula = input( 'Ingrese la cedula del paciente que quiere ingresar en la lista: ' )
        for c in self.__lista_pacientes:
            if cedula == c[1]:
                return print(c)

    def verDatosPacientesDiccionario( self ):
        cedula = input( "Ingresar la cedula del pacientes que busca en el diccionario: " )
        for p, c in enumerate( self.__diccionario_pacientes ):