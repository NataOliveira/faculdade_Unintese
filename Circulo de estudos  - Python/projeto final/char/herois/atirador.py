from char.base_char import BaseChar

class Atirador(BaseChar):

    def __init__(self, nome, hp, ataque, defesa, xp, dano_ultimate, inventario):
        super().__init__(nome, hp, ataque, defesa, xp, dano_ultimate, inventario)
        
    def atacar(self, oponente):
        super().atacar(oponente)
        self._hp = self._hp - self._ataque
        print(f'{self._nome} ataca com seu arco, deferindo \033[31m{self._ataque}\033[0m de dano')

    def ultimate(self, oponente):
        super().ultimate(oponente)
        print(f'\n{self._nome} Usa Ultimate, deferindo \033[31m{self._dano_ultimate}\033[0m de dano')    

    
# MAGOS             NOME   |HP||ATK|DEF||XP||ESPECIAL|
fallen = Atirador('Fallen', 310, 72, 22, 0, 80, [])
garrus = Atirador('Garrus', 280, 75, 16, 0, 95, [])
karl   = Atirador('Karl',   320, 78, 24, 0, 65, [])


lista_atiradores = [fallen,garrus,karl]

