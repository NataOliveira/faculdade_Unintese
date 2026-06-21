from char.base_char  import BaseChar

class MobElite(BaseChar):


    def __init__(self,nome, hp, ataque, defesa, xp,dano_ultimate, inventaio):
        super().__init__(nome, hp, ataque, defesa, xp,dano_ultimate, inventaio)

#--MOB_ELITE                NOME           |HP||ATK|DEF||XP|
orc            = MobElite('Orc',           380, 80, 60, 20 , 100, [])
troll          = MobElite('Troll',         550, 70, 95, 25, 80, [])
vampiro        = MobElite('Vampiro',       420, 75, 55, 22, 90, [])
gargula        = MobElite('Gargula',       340, 90, 70, 20, 120, [])
golem_de_pedra = MobElite('Golem de Pedra',650, 65,160, 28, 60, [])


lista_mob_elite = [orc,troll,vampiro,gargula,golem_de_pedra]
