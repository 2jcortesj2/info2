import pymongo

class Medicamento():
    def __init__(self,client):
        # Creación de la colección principal
        mydb = client["sistVete"] 
        # __medicamentos será el objeto para trabajar sobre "Medicamentos"
        self.__medicamentos = mydb["medicamentos"] 

    def asignarNombre_med(self,nombre_med):
        x = self.__medicamentos.insert_one({'Nombre' : nombre_med})  
    
    def asignarDosis(self,nombre_med,dosis):

        self.__medicamentos.update_one({"Nombre": nombre_med}, {"$set": { "Dosis" : dosis}})
        x = self.__medicamentos.insert_one({'Dosis' : dosis})
    
    def verNombre(self):
        Nombre = list(self.__medicamentos.find())
        return Nombre[-1]['Nombre']
    
    def verDosis(self):
        Dosis=list(self.__medicamentos.find())
        return Dosis[-1]['Dosis']

class Mascota(Medicamento):
    def __init__(self,client):
        mydb = client["sistVete"]
        self.__mascota = mydb["mascota"]
    
    def asignarNombreMasc(self, nombre_masc):
        x=self.__mascota.insert_one({'Nombre':nombre_masc})  
    
    def asignarMedicamento(self, nombre_masc, medicamento):
        Nombre = list(self.__medicamentos.find())
        myquery = {"Nombre": nombre_masc}
        newvalues = { "$set": { "Medicamento": medicamento} }
        self.__medicamentos.update_one(myquery, newvalues)

    def asignarPeso(self, nombre_masc, peso):
        myquery = {"Nombre": nombre_masc}
        newvalues = { "$set": { "Peso": peso} }
        self.__mascota.update_one(myquery, newvalues)

    def asignarFechaIngreso(self,nombre_masc,dosis):
        myquery = {"Nombre": nombre_masc}
        newvalues = { "$set": { "Dosis":dosis} }
        self.__mascota.update_one(myquery, newvalues)

    def asignarTipo(self,nombre_masc,dosis):
        myquery = {"Nombre": nombre_masc}
        newvalues = { "$set": { "Dosis":dosis} }
        self.__mascota.update_one(myquery, newvalues)

    def asignarHistoria(self,nombre_masc,dosis): # fecha y medicamento
        myquery = {"Nombre": nombre_masc}
        newvalues = { "$set": { "Dosis":dosis} }
        self.__mascota.update_one(myquery, newvalues)
    
    def verNombre(self):
        Nombre = list(self.__medicamentos.find())
        return Nombre[-1]['Nombre']
    
    def verNombre(self):
        Nombre = list(self.__medicamentos.find())
        return Nombre[-1]['Nombre']
    
    def verNombre(self):
        Nombre = list(self.__medicamentos.find())
        return Nombre[-1]['Nombre']
    
    def verNombre(self):
        Nombre = list(self.__medicamentos.find())
        return Nombre[-1]['Nombre']
    
    def verNombre(self):
        Nombre = list(self.__medicamentos.find())
        return Nombre[-1]['Nombre']
    
    def verNombre(self):
        Nombre = list(self.__medicamentos.find())
        return Nombre[-1]['Nombre']

class Sistema(Mascota):
    def eliminarMascota():
        pass

    def vermedicamentos():
        pass

    def ingresarMascota():
        pass

    def verfechaIngreso():
        pass

    def verNumeromascota():
        pass

    def salir():
        pass
        
def main():

    client = pymongo.MongoClient("mongodb+srv://jjosecortes:jjosecortes@info2.1k5lrgf.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    nm=int(input("Ingrese la cantidad de medicamento de la mascota: "))
    m=0
    while m<nm:
        nombre_medicamentos = input("Ingrese el nombre: ") 
        dosis = int(input("Ingrese la dosis: ")) 
        medicamento = Medicamento(client) 
        medicamento.asignarNombre(nombre_medicamentos)
        ultimo_nombre = medicamento.verNombre()
        print(ultimo_nombre)
        medicamento.asignarDosis(ultimo_nombre,dosis)
        print(medicamento.verDosis())
        m+=1
        
def main22():
    #creamos el sistema
    sistema = Sistema()
    while True:
        opcion = ingresoNumerico("Ingrese 0 para salir, 1 para ingresar mascota, 2 para eliminar, 3 ver Fecha Ingreso, 4 ver lista medicamentos, 5 ver numero de mascotas ")
        if opcion == 0:
            print("Fin del programa ...")
            break
        elif opcion == 5:
            print("El sistema tiene " + str(sistema.verNumeroMascotas()) + " mascotas")
        elif opcion == 4:
            #1. solicitar numero de historia clinica y ver que no este
            nhc = int(input("Ingrese Numero de Historia Clinica: "))
            if sistema.verificarMascota(nhc) == False:
                print("La mascota no esta en el sistema ...")
                continue
            #recupero la mascota de la base de datos
            m = sistema.recuperarMascota(nhc)
            lista_medicamentos = m.verMedicamentos()
            print("La mascota: " + m.verNombre() + " tiene los sgtes medicamentos:")
            for medicamento in lista_medicamentos:
                print("Medicamento con nombre: " + medicamento.verNombre() + " dosis " + str(medicamento.verDosis()))
        elif opcion == 3:
            #1. solicitar numero de historia clinica y ver que no este
            nhc = int(input("Ingrese Numero de Historia Clinica: "))
            if sistema.verificarMascota(nhc) == False:
                print("La mascota no esta en el sistema ...")
                continue
            print(sistema.verFechaIngresoMascota(nhc))
        elif opcion == 2:
            #1. solicitar numero de historia clinica y ver que no este
            nhc = int(input("Ingrese Numero de Historia Clinica: "))
            resultado = sistema.eliminarMascota(nhc)
            if resultado == True:
                print("Se elimino exitosamente la mascota del sistema ...")
            else:
                print("No se elimino la mascota del sistema, posiblemente no exista ...")
        elif opcion == 1:
            #1. debo verificar que haya espacio en el servicio
            if sistema.verNumeroMascotas() >= 10:
                print("No hay espacio ...")
                continue
            #2. solicitar numero de historia clinica y ver que no este
            nhc = ingresoNumerico("Ingrese Numero de Historia Clinica: ")
            if sistema.verificarMascota(nhc) == True:
                print("La mascota ya esta en el sistema ...")
                continue
            #3. Si la historia no esta pido los datos restantes
            n = input("Ingrese el nombre de la mascota: ")
            t = input("Ingrese CANINO o FELINO: ")
            p = ingresoNumerico("Ingrese el pesos de la mascota en kilogramos")
            f = input("Ingrese la fecha dd/mm/aaaa : ")
            nm = int(input("Ingrese el numero de medicamentos: "))
            lista_medicamentos = []
            #4. por cada medicamento solicito los datos
            for i in range(0,nm):
                nombre_medicamentos = input("Ingrese el nombre: ")
                dosis = ingresoNumerico("Ingrese la dosis: ")
                medicamento = Medicamento()
                medicamento.asignarDosis(dosis)
                medicamento.asignarNombre(nombre_medicamentos)
                lista_medicamentos.append(medicamento)
            #5. crear la mascota y asignarle la informacion
            mascota = Mascota()
            mascota.asignarHistoria(nhc)
            mascota.asignarNombre(n)
            mascota.asignarTipo(t)
            mascota.asignarPeso(p)
            mascota.asignarFechaIngreso(f)
            mascota.asignarMedicamentos(lista_medicamentos)
            #6. Ingresar la mascota al sistema
            sistema.ingresarMascota(mascota)
            print("Mascota " + n + " ingresada ...")
        else:
            print("Opcion no valida: ")

if __name__ == '__main__':
    main()