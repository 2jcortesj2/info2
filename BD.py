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
        self.__genero = input('Ingrese género del ' + rol + ': ')
    
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
        self.__lista_pacientes = [('Juan', '123', 'M'), ('Mauricio', '456', 'M')]
        self.__lista_nombre = ['Juan', 'Mauricio']
        self.__lista_cedula = ['123', '456']
        self.__lista_genero = ['M', 'M']
        self.__diccionario_pacientes = {'Nombre': ['Juan', 'Mauricio'], 'Cedula': ['123', '123'], 'Genero': ['M', 'M']}

    def numeroPacientes(self):
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
        print(self.__lista_cedula)
        print(self.__lista_genero)
        print(self.__diccionario_pacientes)
        print(self.numeroPacientes())

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
                Nombre:  {self.__diccionario_pacientes['Nombre'][p]} 
                cedula : {self.__diccionario_pacientes['Cedula'][p]} 
                Genero:  {self.__diccionario_pacientes['Genero'][p]}''')


                
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
            a.verDatosPacientesDiccionario()
        if opcion == 3:
            print(f'Número de pacientes registrados: {a.numeroPacientes()}')
        if opcion == 4:
            break

if __name__ == '__main__':
    main()