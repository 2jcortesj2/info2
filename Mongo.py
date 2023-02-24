import pymongo

client = pymongo.MongoClient("mongodb+srv://jjosecortes:jjosecortes@info2.1k5lrgf.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# Se crea la base de datos con su nombre
mydb = client["bbdd"]

# Se crean subconjuntos
mycol = mydb["clientes"]
myprov = mydb["proovedores"]

# se define la información
mydict_client = {"nombre": "Juan", "direccion": "c/ Mayor 1"}
mydict_prov = {"nombre": "Carlos", "direccion": "c/ Mayor 2"}

# Se guarda en la red
x = mycol.insert_one(mydict_client)
y = myprov.insert_one(mydict_prov)

print(x.inserted_id)
print(y.inserted_id)

for x in mycol.find({'nombre': 0}):
    print(x)

for y in myprov.find():
    print(y)

myquery = {"nombre": "Juan", "direccion": "c/ Mayor 1"}
newvalues = {"$set": {"nombre": "Luis"}}

