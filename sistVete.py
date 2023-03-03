import pymongo

class Medicamento():
    def __init__(self,client):
        mydb = client["sistVete"]
        self.__medicamentos = mydb["medicamentos"]
    
    def verNombre(self):
        Nombre = list(self.__medicamentos.find())
        return Nombre[-1]['Nombre']
    
    def verDosis(self):
        Dosis=list(self.__medicamentos.find())
        print('La dosis suministrada es: ' + str(Dosis[-1]['Dosis']))

    def asignarNombre_med(self,nombre_med):
        x=self.__medicamentos.insert_one({'Nombre':nombre_med})  
    
    def asignarDosis(self,nombre_med,dosis):
        myquery = {"Nombre": nombre_med}
        newvalues = { "$set": { "Dosis":dosis} }
        self.__medicamentos.update_one(myquery, newvalues)
        #self.__medicamento = self.__medicamentos.insert_one({'Dosis':dosis})

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
        #medicamento.asignarNombreDosis(nombre_medicamentos,dosis)
        medicamento.asignarNombre(nombre_medicamentos)
        ultimo_nombre=medicamento.verNombre()
        print(f'El nombre del medicamento es {ultimo_nombre}')
        medicamento.asignarDosis(ultimo_nombre,dosis)
        medicamento.verDosis()
        m+=1


if __name__=='__main__':
    main()
