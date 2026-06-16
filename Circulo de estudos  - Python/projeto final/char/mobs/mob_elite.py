from char.base_char  import BaseChar

class MobElite(BaseChar):


    def __init__(self,nome,hp,ataque,defesa, xp_drop):
        super().__init__(nome,hp,ataque,defesa, xp_drop)

#--MOB_ELITE                NOME           |HP||ATK|DEF||XP|
orc            = MobElite('Orc',           380, 120, 60, 20)
troll          = MobElite('Troll',         550, 140, 95, 25)
vampiro        = MobElite('Vampiro',       420, 145, 55, 22)
gargula        = MobElite('Gargula',     340, 130, 70, 20)
golem_de_pedra = MobElite('Golem de Pedra',650,  95,160, 28)


lista_mob_elite = [orc,troll,vampiro,gargula,golem_de_pedra]
