import pymongo

class Medicamento:

    def _init_( self, client ):
        my_data_base = client[ "Tarea" ]
        self.__medicamentos = my_data_base[ "Medicamentos" ]

    # ELIMINAMOS LOS METODOS DE VER YA QUE NO SON NECESARIOS

    # METODOS PARA ASIGNAR
    def MedicamentoAsignarNombre( self, nombre_med ):
        medicamento = { "Nombre medicamento": nombre_med }
        self.__medicamentos.insert_one( medicamento )

    def MedicamentoAsignarDosis( self, nombre_med, dosis_med ):
        my_medicamento = { "Nombre medicamento": nombre_med }
        my_dosis = { "$set" : { "Dosis": dosis_med } }
        self.__medicamentos.update_one( my_medicamento, my_dosis )
    
    def MedicamentoAsignarNumeroHistoria( self, nombre_med, num_historia ):
        my_medicamento = { "Nombre medicamento": nombre_med }
        my_historia = { "$set": { "Historia": num_historia } }
        self.__medicamentos.update_one( my_medicamento, my_historia )


class Mascota:

    def _init_( self, client, historia ):
        my_data_base = client[ "Tarea" ]
        self.__mascota = my_data_base[ "Mascota" ]
        self.__historia = historia

    # ELIMINAMOS LOS METODOS DE VER YA QUE NO SON NECESARIOS

    # Metodos para asignar
    def MascotaAsignarNombre( self, nombre ):
        histo = { "Historia": self.__historia }
        lista = { "$set": { "Nombre": nombre } }
        self.__mascota.update_one( histo, lista )

    def MascotaAsignarHistoria( self ):
        histo = { "Historia": self.__historia }        
        self.__mascota.insert_one( histo )

    def MascotaAsignarTipo( self, tipo ):    
        histo = { "Historia": self.__historia }
        lista = { "$set": { "Gato o Perro": tipo } }
        self.__mascota.update_one( histo, lista )

    def MascotaAsignarFechaIngreso( self, fecha ):
        histo = { "Historia": self.__historia }
        lista = { "$set": { "Fecha": fecha } }
        self.__mascota.update_one( histo, lista )

    def MascotaAsignarPeso( self, peso ):
        histo = { "Historia": self.__historia }
        lista = { "$set": { "Peso": peso } }
        self.__mascota.update_one( histo, lista )

    def MascotaAsignarMedicamento( self, medicamento ):
        histo = { "Historia": self.__historia }
        lista = { "$set": { "Medicamento": medicamento } }
        self.__mascota.update_one( histo, lista )


class Sistema:

    def _init_( self, client ):
        my_data_base = client[ "Tarea" ]
        self.__mascota = my_data_base[ "Mascota" ]
        self.__medicamentos = my_data_base[ "Medicamentos" ]

    def SistemaEliminarMascota( self, numHisCli ):
        lista = list( self.__mascota.find( { "Historia": numHisCli } ) )
        self.__mascota.delete_one( lista[-1] )
        lista2 = list( self.__medicamentos.find( { "Historia": numHisCli } ) )
        for eliminar in lista2:
            self.__medicamentos.delete_one( eliminar )

    def SistemaVerMedicamento( self, numHisCli ): # que se esta aministrando a una mascota
        medicamentos = list( self.__medicamentos.find( { "Historia": numHisCli } ) )
        for medicamento in medicamentos:
            print( f" Nombre medicamneto: { medicamento['Nombre medicamento'] }, Dosis: { medicamento['Dosis'] } " )
            
    def SistemaVerFechaIngreso( self, numHisCli ):
        lista = list( self.__mascota.find( { "Historia": numHisCli } ) )
        try:
            print( lista[-1][ "Fecha" ] )
        except:
            print( "No hay ninguna fecha de ingreso registrada con ese numero de historia clinica" )        
    def SistemaVerNumeroDeMascotas( self ):
        lista = list( self.__mascota.find() )
        return len( lista )

    # ESTE METODO SIRVE SI SE QUIERE SALIR POR MEDIO DE ESTE, YO PUSE UN BREAK
    # def salir( self, bandera ): 
    #     bandera = False
    #     return bandera


    # ALGUNOS METODOS ADICIONALES PARA QUE EL CODIGO SEA MAS FUNCIONAL

    def SistemaVerificarMascota( self, numHisCli ):
        lista = list( self.__mascota.find( { "Historia": numHisCli } ) )
        if len( lista ) == 0:
            return False
        else: 
            return True 

######################## METODO VALIDAR INT ################################

def validarInt( a ):
    try:
        a = int( a )
        return a
    except:
        b = input( "Ingrese un numero entero: " )
        validarInt( b )

############################################################################


def main():

    client = pymongo.MongoClient( "mongodb+srv://josuepaniagua:Ba5319466531@cluster0.megrtoc.mongodb.net/?retryWrites=true&w=majority" )
    db = client.test

    sistema = Sistema( client )

    while True:

        opcion = input( """
        (0) Salir
        (1) Ingresar mascota
        (2) Eliminar mascota
        (3) Fecha de ingreso de la mascota
        (4) Ver lista de medicamentos
        (5) Ver numero de mascotas
        > """ )

        if opcion == '0':
            print( "Fin del programa..." )
            break

        elif opcion == '1': # INGRESAR MASCOTA
            
            if sistema.SistemaVerNumeroDeMascotas() >= 10:
                print( "No hay espacio" )
                continue

            num_historia = validarInt( input("Ingrese el numero de la historia clinica de la mascota: ") )
            if sistema.SistemaVerificarMascota( num_historia ) ==  True:
                print( "El numero de historia clinica ya esta registrado" )
                continue
                
            name = input( "Ingrese el nombre de la mascota: " )
            type = input( "Ingrese CANINO o FELINO: " )
            weight = input( "Ingrese el peso de la mascota en Kilogramos: " )
            date = input( "Ingrese la fecha dd/mm/aaaa: " )
            med_num = validarInt( input( "Ingrese la cantidad de medicamentos: " ) )

            for i in range( 0, med_num ):
                medicamento = Medicamento( client )
                nombre_medicamento = input( "Ingrese el nombre del medicamento: " )
                dosis = input( "Ingrese la dosis del medicamento: " )
                medicamento.MedicamentoAsignarNombre( nombre_medicamento )
                medicamento.MedicamentoAsignarDosis( nombre_medicamento, dosis )
                medicamento.MedicamentoAsignarNumeroHistoria( nombre_medicamento, num_historia )
            
            pet = Mascota( client, num_historia )
            pet.MascotaAsignarHistoria()
            pet.MascotaAsignarNombre( name )
            pet.MascotaAsignarTipo( type )
            pet.MascotaAsignarPeso( weight )
            pet.MascotaAsignarFechaIngreso( date )

            print( f"Mascota {name} ingresada..." )

        elif opcion == '2': # ELIMINAR MASCOTA
            
            num_historia = validarInt( input( "Ingrese el numero de la historia clinica que desea eliminar: " ) )
            if sistema.SistemaVerificarMascota( num_historia ) == False:
                print( "El numero de la historia clinica ingresado no existe..." )
                continue

            sistema.SistemaEliminarMascota( num_historia )
            print( "Mascota eliminada..." )
        
        elif opcion == '3': # FECHA DE INGRESO DE LA MASCOTA
            
            num_historia = validarInt( input( "Ingrese el numero de la historia clinica que desea ver la fecha de ingreso: " ) )
            if sistema.SistemaVerificarMascota( num_historia ) == False:
                print( "El numero de la historia clinica ingresado no existe..." )
                continue

            sistema.SistemaVerFechaIngreso( num_historia )


        elif opcion == '4': # VER LISTA DE MEDICAMENTOS (que se esta administrando a una mascota)
            
            num_historia = validarInt( input( "Numero de historia de la mascota a la que le desea ver los medicamentos: " ) )
            if sistema.SistemaVerificarMascota( num_historia ) == False:
                print( "El numero de la historia clinica ingresado no existe..." )
                continue

            sistema.SistemaVerMedicamento( num_historia )
            

        elif opcion == '5': # VER NUMERO DE MASCOTAS
        
            print( sistema.SistemaVerNumeroDeMascotas() )

        else:
            print( "Opcion no valida" )

if __name__ == '_main_':
    main()