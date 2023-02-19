class Persona:
    def __init__(self):
        self.__nombre = ''
        self.__cedula = ''
        self.__genero = ''
    
    def asignarNombre(self, rol):
        self.__nombre = input('Ingrese nombre del ' + rol + ': ')
    
    def asignarCedula(self, rol):
        self.__cedula = input('Ingrese cedula del ' + rol + ': ')

    def asignarGenero(self, rol):
        self.__genero = input('Ingrese genero del ' + rol + ': ')
    
    def verNombre(self):
        return self.__nombre
    
    def verCedula(self):
        return self.__cedula
    
    def verGenero(self):
        return self.__genero
    
    def guardarInfo(self):
        return self.__nombre, self.__cedula, self.__genero

class Paciente(Persona):
    def __init__(self):
        self.__servicio = ''

    def asignarServicio(self):
        self.__servicio = input('Ingresar servicio: ')

    def verServicio(self):
        return self.__servicio
    
class Empleado(Persona):
    def __init__(self):
        self.__turno = ''

    def asignarTurno(self, turno):
        self.__turno = turno

    def verTurno(self, turno):
        return self.__turno

class Enfermera(Empleado):
    def __init__(self):
        self.__rango = ''

    def asignarRango(self, rango):
        self.__rango = rango

    def verRango(self):
        return self.__rango

class Medico(Empleado):
    def __init__(self):
        self.__especialidad = ''

    def asignarEspecialidad(self, especialidad):

        self.__especialidad = especialidad
    def verEspecialidad(self):
        return self.__especialidad

class Sistema(Persona):
    def __init__(self): # No puse doble guion
        self.__lista_pacientes = []
        self.__lista_nombre = []
        self.__lista_cedula = []
        self.__lista_genero = []
        self.__diccionario_pacientes = {  }

    def numeroDePacientes(self):
        self.__numero_pacientes = len(self.__lista_pacientes)
        return self.__numero_pacientes
    
    def ingresarPaciente(self, rol):
        p = Paciente() 
        p.asignarNombre(rol)
        p.asignarGenero(rol)
        p.asignarCedula(rol)
        p.asignarServicio()
        self.__lista_pacientes.append(p.guardarInfo())
        self.__lista_nombre.append(p.verNombre())
        self.__lista_cedula.append(p.verCedula())
        self.__lista_genero.append(p.verGenero())
        self.__diccionario_pacientes.update({'Nombre' : self.__lista_nombre, 
        'Cedula' : self.__lista_cedula, 'Genero' : self.__lista_genero})

        print(self.__lista_pacientes)
        print(self.numeroDePacientes())

    def verDatosPacientesLista(self):
        cedula = input('Ingrese la cedula del paciente que quiere ingresar en la lista: ')
        for c in self.__lista_pacientes:
            if cedula == c[1]:
                return print(c)

    def verDatosPacientesDiccionario(self):
        cedula = input('Ingresar la cedula del paciente: ')
        for p, c in enumerate(self.__diccionario_pacientes['Cedula']):
            if cedula == c:
                print(f'''
                Nombre: {self._diccionario_pacientes['Nombre'][p]}, 
                cedula : {self.diccionario_pacientes['Cedula'][p]}, 
                Genero: {self._diccionario_pacientes['Genero'][p]}''')


                
def main():
    a = Sistema()                
    while True:
        opcion = int(input('''
        1. Ingresar paciente
        2. Ver datos de paciente
        3. Ver numero de pacientes
        4. Salir
        >> '''))
        if opcion == 1:
            a.ingresarPaciente('Paciente')
        if opcion == 2:
            a.verDatosPacientesDiccionario('Paciente')
        if opcion == 3:
            a.numeroDePacientes('Paciente')
        if opcion == 4:
            break

if __name__ == '__main__':
    main()