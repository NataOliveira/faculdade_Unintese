from char.base_char import BaseChar

class Mago(BaseChar):
    
    def __init__(self, nome, hp, ataque, defesa, xp, ataque_especial):
        super().__init__(nome, hp, ataque, defesa, xp)
        self.ataque_especial = ataque_especial

# MAGOS          NOME    |HP||ATK|DEF||XP||ESPECIAL|
merlin  = Mago('Merlin',  280, 55, 15, 0, 96)
morgana = Mago('Morgana', 260, 48, 12, 0, 105)
gandalf = Mago('Gandalf', 350, 65, 25, 0, 85)

lista_soldados = [merlin, morgana, gandalf]