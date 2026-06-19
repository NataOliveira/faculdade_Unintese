from char.base_char import BaseChar

class Atirador(BaseChar):

    def __init__(self, nome, hp, ataque, defesa, xp, dano_ultimate, inventario):
        super().__init__(nome, hp, ataque, defesa, xp, dano_ultimate, inventario)
        

# MAGOS             NOME   |HP||ATK|DEF||XP||ESPECIAL|
fallen = Atirador('Fallen', 310, 72, 22, 0, 80, [])
garrus = Atirador('Garrus', 280, 75, 16, 0, 95, [])
karl   = Atirador('Karl',   320, 78, 24, 0, 65, [])


lista_atiradores = [fallen,garrus,karl]

