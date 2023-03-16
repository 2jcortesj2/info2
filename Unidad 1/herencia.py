class ave:
    # Constructor de ave en su forma mas abstracta o básica
    def __init__(self, tipo, vuela):
        self.ave = tipo # referente si es carnivora, insectivora, omnivora, carroñera, etc
        self.vuelo = vuela
        self.oviparos = True
        self.pico = True
    
    # Acciones básicas
    def comer(self, comida):
        print("Este tipo de ave come normalmente: ", comida)

    def volar(self):
        print("Este tipo de ave puede volar: ", self.vuelo)

class ganso(ave):
    def __init__(self, tipo, vuela, accion, pata):
        # Invocar al constructor de clase ave
        ave.__init__(self, tipo, vuela)
        # Nuevos atributos
        self.habilidad = accion # Puede volar y/o nadar
        self.patas = pata

    def destreza(self):
        print("Esta ave puede: ", self.habilidad)

class pato(ganso):
    pass

class gallina(ave):
    pass

p = ave("gallina", False)
p.volar()
p.comer("Maiz")

g = ganso("carnivoro", True, "nadar", 4)
g.destreza()