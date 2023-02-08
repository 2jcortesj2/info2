class ave:
    # Constructor de ave en su forma mas abstracta o básica
    def __init__(self, tipo, vuela):
        self.ave = tipo # referente si es carnivora, insectivora, omnivora, carroñera, etc
        self.vuelo = vuela
        self.oviparos = True
        self.pico = True
    
    # Acciones básicas
    def comer(self, comida):
        print("Este tipom de ave come normalmente: ", comida)

    def volar(self):
        print("Este tipo de ave puede volar: ", self.vuelo)

class ganso(ave):
    def __init__(self, tipo)