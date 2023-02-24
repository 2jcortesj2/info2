import pymongo

client = pymongo.MongoClient("mongodb+srv://jjosecortes:jjosecortes@info2.1k5lrgf.mongodb.net/?retryWrites=true&w=majority")
db = client.test

mydb = client["bbdd"]
mycol = mydb["clientes"]
myprov = mydb["proovedores"]

mydict_client = {"nombre": "Juan", "direccion": "c/ Mayor 1"}
mydict_prov = {"nombre": "Carlos", "direccion": "c/ Mayor 2"}

x = mycol.insert_one(mydict_client)
print(x.inserted_id)