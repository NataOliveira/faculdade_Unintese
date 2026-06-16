from char.base_char import BaseChar

class Soldado(BaseChar):
    
    def __init__(self, nome, hp, ataque, defesa,  xp, ataque_especial):
        super().__init__(nome, hp, ataque, defesa, xp)
        self.ataque_especial = ataque_especial

 
# SOLDADOS              NOME       |HP||ATK|DEF||XP||ESPECIAL|
aquiles    = Soldado('Aquiles',     350, 75, 32, 0, 120)
joana_darc = Soldado("Joana d'Arc", 340, 62, 38, 0, 140)
leonidas   = Soldado('Leônidas',    390, 65, 45, 0, 100)

lista_soldados = [aquiles,joana_darc,leonidas]