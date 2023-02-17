class Cosa:
    def __init__(self, publico:str = "publico", protegido: str = "protegido", privado: str = "privado"):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado
    
    def informacion(self):
        print(
            (
                f"Esta es una clase con atributos publicos: {self.publico}"
                f"\nun atributo protegido: {self._protegido}"
                f"\ny un archivo privado: {self.__privado}"
            )
        )
    
a = Cosa()

A = {1:'hola', 2:'como', 3:'te'}
B = { 1:'llamas', 5:'tu', 6:'nombre'}

A.update(B)
print(A)

#for p, c in enumerate(A):
 #   print(p)
  #  print('\n',c)