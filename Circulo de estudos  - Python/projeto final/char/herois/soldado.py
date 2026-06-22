from char.base_char import BaseChar
import msvcrt

class Soldado(BaseChar):
    
    def __init__(self, nome, hp, ataque, defesa,  xp, dano_ultimate,inventario):
        super().__init__(nome, hp, ataque, defesa, xp, dano_ultimate,inventario)
        
    def atacar(self, oponente):
        super().atacar(oponente)
        print(f'\n{self._nome} ataca com sua espada, deferindo \033[31m{self._ataque}\033[0m de dano')

    def ultimate(self, oponente):
        super().ultimate(oponente)
        print(f'\n{self._nome} Usa Ultimate, deferindo \033[31m{self._dano_ultimate}\033[0m de dano')
    
       

# SOLDADOS              NOME       |HP||ATK|DEF||XP||ESPECIAL|
aquiles    = Soldado('Aquiles',     2500, 65, 32, 0, 150,  [])
joana_darc = Soldado("Joana d'Arc", 340, 75, 38, 0, 140,  [])
leonidas   = Soldado('Leônidas',    390, 50, 45, 0, 110,  [])

lista_soldados = [aquiles,joana_darc,leonidas]


