from char.base_char import BaseChar
from random import randint

class MobFraco(BaseChar):

    def __init__(self,nome, hp, ataque, defesa, xp,dano_ultimate, inventaio):
        super().__init__(nome, hp, ataque, defesa, xp,dano_ultimate, inventaio)
        
#--MOB_FRACO                NOME           |HP|           |ATK|DEF||XP|
goblin         = MobFraco('Goblin',        150,  randint(50,75), 20,  5, 0, [])
zumbi          = MobFraco('Zumbi',         180,  randint(50,75), 20,  8, 0, [])
esqueleto      = MobFraco('Esqueleto',     140,  randint(50,75), 25,  7, 0, [])
lobo_selvagem  = MobFraco('Lobo Selvagem', 220,  randint(50,75), 15,  8, 0, [])

lista_mob_fraco = [goblin,zumbi,esqueleto,lobo_selvagem]

