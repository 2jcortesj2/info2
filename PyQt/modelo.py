# Trasferencia de datos

import pymongo

uri = "mongodb+srv://jjosecortes:jjosecortes@info2.1k5lrgf.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client.test

class Sistema():
    def __init__ (self,client):
        mydb = client["Hospital"]
        self.__neurologia = mydb["neurologia"]

    def verificar_db(self,cedula):
        x = self.__neurologia.find_one({'Cedula':int(cedula)})
        if x == None:
            return None, None
        else:
            return x['Nombre'],x[ 'Edad']

    def set_cedula(self,cedula):
        self.__neurologia.insert_one({'Cedula':cedula})

    def set_nombre(self,cedula,nombre):
        myquery = {'Cedula':cedula}
        newvalues = {"$set": {"Nombre":nombre}}
        self.__neurologia.update_one(myquery, newvalues)

    def set_edad(self,cedula, edad):
        myquery = {'Cedula':cedula}
        newvalues = {"$set": {"Edad":edad}}
        self.__neurologia.update_one(myquery, newvalues)