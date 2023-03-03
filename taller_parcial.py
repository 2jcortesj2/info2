import pymongo

class Medicamento:
    def _init_(self,client):
        mydb = client["sisVete"]
        self.__medicamentos = mydb["medicamentos"]

    def verNombre(self):
        for x in self.__medicamentos.find({"nombre"}):
            return print(x)
        
    def asignarNombreDosis(self,nombre_med,dosis):
        self._medicamento = self._medicamentos.insert_one({"nombre":nombre_med,"dosis":dosis})
        return self.__medicamento
        
        
def main():
    client = pymongo.MongoClient("mongodb+srv://jjosecortes:jjosecortes@info2.1k5lrgf.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    nm = int(input("ingrese la cantidad de medicamentos de la mascota: "))
    n = 0
    while n<nm:
        nombre_medicamentos = input("ingrese el nombre del medicamento : ")
        dosis = int(input("ingrese el # de dosis: "))
        medicamento = Medicamento(client)
        medicamento.asignarNombreDosis(nombre_medicamentos,dosis)
        medicamento.verNombre("dolex")
        n+=1

if _name_ == "_main_":
    
    main()