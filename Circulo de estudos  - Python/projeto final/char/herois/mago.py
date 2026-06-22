from char.base_char import BaseChar

class Mago(BaseChar):
    
    
    def __init__(self, nome, hp, ataque, defesa, xp, mana, dano_ultimate, inventario):
        super().__init__(nome, hp, ataque, defesa, xp, dano_ultimate, inventario)
        self._mana = mana
        
    def atacar(self, oponente):
        super().atacar(oponente)
        print(f'{self._nome} ataca com sua magia, deferindo \033[31m{self._ataque}\033[0m de dano') 

    def ultimate(self, oponente):
        super().ultimate(oponente)
        print(f'\n{self._nome} Usa Ultimate, deferindo \033[31m{self._dano_ultimate}\033[0m de dano')   

# MAGOS          NOME    |HP||ATK|DEF||XP|Mana|ESPECIAL|Inventário
merlin  = Mago('Merlin',  280, 55, 15, 0, 100, 96, [])
morgana = Mago('Morgana', 260, 48, 12, 0, 110, 105,[])
gandalf = Mago('Gandalf', 350, 65, 25, 0, 90, 85,[])

lista_magos = [merlin, morgana, gandalf]

