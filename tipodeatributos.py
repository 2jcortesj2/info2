class Cosa:
    def __init__(self, publico:str = "publico", protegido: str = "protegido", privado: str = "privado"):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado
    
    def informacion(self):
        print(
            (
                f"Esta es uan clase con atributos publicos: {self.publico}"
                f"un atributo protegido: {self._protegido}"
                f"y un archivo privado: {self.__privado}"
            )
        )
    
a = Cosa()

print(a.__privado)