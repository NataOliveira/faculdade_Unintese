from char.base_char import BaseChar
from random import randint

class Soldado(BaseChar):
    
    def __init__(self, nome, hp, ataque, defesa,  xp, dano_ultimate,inventario):
        super().__init__(nome, hp, ataque, defesa, xp, dano_ultimate,inventario)
        

 
# SOLDADOS              NOME       |HP||ATK|DEF||XP||ESPECIAL|
aquiles    = Soldado('Aquiles',     3500, 65, 32, 0, 150,  [])
joana_darc = Soldado("Joana d'Arc", 340, 75, 38, 0, 140,  [])
leonidas   = Soldado('Leônidas',    390, 50, 45, 0, 110,  [])

lista_soldados = [aquiles,joana_darc,leonidas]