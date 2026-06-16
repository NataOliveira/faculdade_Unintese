from char.base_char import BaseChar

class MobFraco(BaseChar):

    def __init__(self,nome, hp, ataque, defesa, xp_drop):
        super().__init__(nome, hp, ataque, defesa, xp_drop)
        
#--MOB_FRACO                NOME           |HP||ATK|DEF||XP|
goblin         = MobFraco('Goblin',        150,  50, 20,  5)
zumbi          = MobFraco('Zumbi',         180,  55, 20,  5)
esqueleto      = MobFraco('Esqueleto',     140,  65, 25,  5)
lobo_selvagem  = MobFraco('Lobo Selvagem', 220,  80, 15,  8)

lista_mob_fraco = [goblin,zumbi,esqueleto,lobo_selvagem]

