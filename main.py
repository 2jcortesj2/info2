import pymongo
from sistVete import Medicamento

client = pymongo.MongoClient("mongodb+srv://jjosecortes:jjosecortes@info2.1k5lrgf.mongodb.net/?retryWrites=true&w=majority")
db = client.test

x = Medicamento(client)

x.asignarNombre_med('Penicilina')
x.asignarDosis('Penicilina', 23)
print(x.verNombre())
print(x.verDosis())