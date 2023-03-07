import pymongo

class Medicamento:
    def __init__(self, client):
        # Creación de la colección principal
        mydb = client["sistVete"] 
        self.__medicamentos = mydb["medicamentos"] 
    
    def asignarNombreMed(self, nombre_med):
        self.__medicamentos.insert_one({'Nombre': nombre_med})  
    
    def asignarDosis(self,nombre_med, dosis):
        self.__medicamentos.update_one({"Nombre": nombre_med}, {"$set": { "Dosis": dosis}})

class Mascota:
    def __init__(self, client):
        mydb = client["sistVete"] 
        self.__mascota = mydb["mascota"]
        self.__medicamentos = mydb["medicamentos"] 
    
    def asignarNombreMasc(self, nombre_masc):
        self.__mascota.insert_one({'NombreMascota':nombre_masc})  

    def asignarPeso(self, nombre_masc, peso):
        myquery = {"NombreMascota": nombre_masc}
        newvalues = {"$set": { "Peso": peso}}
        self.__mascota.update_one(myquery, newvalues)

    def asignarFechaIngreso(self, nombre_masc, fecha):
        myquery = {"NombreMascota": nombre_masc}
        newvalues = {"$set": {"Fechaingreso": fecha}}
        self.__mascota.update_one(myquery, newvalues)

    def asignarTipo(self, nombre_masc, tipo):
        myquery = {"NombreMascota": nombre_masc}
        newvalues = { "$set": {"Tipo": tipo}}
        self.__mascota.update_one(myquery, newvalues)

    def asignarMedicamentos(self, nombre_masc, Meddict):
        myquery = {"NombreMascota": nombre_masc}
        newvalues = {'$set': Meddict}
        self.__mascota.update_one(myquery, newvalues)

    def asignarHistoria(self, nombre_masc, nhc):
        myquery = {"NombreMascota": nombre_masc}
        newvalues = {'$set': {"Tipo": nhc}}
        self.__mascota.update_one(myquery, newvalues)


class Sistema(Mascota):
    def __init__(self, client):
        mydb = client["sistVete"] 
        self.__mascotas = mydb["mascota"]
        self.__medicamentos = mydb["medicamentos"]
    
    def eliminarMascota():
        pass

    def verMedicamentos():
        pass

    def verFechaIngreso(self, nombre_masc):
        pass

    def verNumeroMascotas(self):
        return len(list(self.__mascotas.find()))
    
    def verificarMascota(self, nhc):
        return list(self.__mascotas.find({'nhc': nhc}))


def ingresoNumerico(msg=''):
  try:
    valor_numerico = int(input(msg))
    return valor_numerico
  except:
    print("Por favor ingresar solo números.")
    return ingresoNumerico(msg)

def main():
    client = pymongo.MongoClient("mongodb+srv://jjosecortes:jjosecortes@info2.1k5lrgf.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    #creamos el sistema
    sistema = Sistema(client)
    while True:
        opcion = ingresoNumerico("""Ingrese: 
        0-Salir
        1-Ingresar mascota
        2-Eliminar
        3-Ver Fecha Ingreso
        4-Ver lista medicamentos
        5-Ver numero de mascotas
        >> """)
        if opcion == 0:
            print("Fin del programa ...")
            break

        elif opcion == 5:
            print("\nEl sistema tiene " + str(sistema.verNumeroMascotas()) + " mascotas")

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
            t = input("Ingrese CANINO o FELINO (C/F): ")
            p = ingresoNumerico("Ingrese el pesos de la mascota en kilogramos: ")
            f = input("Ingrese la fecha dd/mm/aaaa : ")
            nm = int(input("Ingrese el número de medicamentos: "))
            lista_medicamentos = {}
            #4. por cada medicamento solicito los datos
            for i in range(0,nm):
                nombre_medicamentos = input("\nIngrese el nombre: ")
                dosis = ingresoNumerico("Ingrese la dosis: ")
                medicamento = Medicamento(client)
                medicamento.asignarNombreMed(nombre_medicamentos)
                medicamento.asignarDosis(nombre_medicamentos, dosis)
                lista_medicamentos[nombre_medicamentos] = (dosis)
            #5. crear la mascota y asignarle la informacion
            mascota = Mascota(client)
            mascota.asignarNombreMasc(n)
            # mascota.asignarHistoria(n, nhc)
            mascota.asignarTipo(n, t)
            mascota.asignarPeso(n, p)
            mascota.asignarFechaIngreso(n, f)
            mascota.asignarMedicamentos(n, lista_medicamentos)
            #6. Ingresar la mascota al sistema
            # sistema.ingresarMascota(mascota) ###############################
            print("Mascota " + n + " ingresada ...")
        
        else:
            print("Opcion no valida: ")

if __name__ == '__main__':
    main()