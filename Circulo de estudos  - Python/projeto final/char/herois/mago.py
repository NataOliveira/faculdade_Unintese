from char.base_char import BaseChar

class Mago(BaseChar):
    
    
    def __init__(self, nome, hp, ataque, defesa, xp, mana, dano_ultimate, inventario):
        super().__init__(nome, hp, ataque, defesa, xp, dano_ultimate, inventario)
        self.mana = mana
        
        

# MAGOS          NOME    |HP||ATK|DEF||XP|Mana|ESPECIAL|
merlin  = Mago('Merlin',  280, 55, 15, 0, 100, 96, [])
morgana = Mago('Morgana', 260, 48, 12, 0, 110, 105,[])
gandalf = Mago('Gandalf', 350, 65, 25, 0, 90, 85,[])

lista_magos = [merlin, morgana, gandalf]