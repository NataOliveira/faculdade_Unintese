from char.base_char  import BaseChar
from random import randint

class MobElite(BaseChar):


    def __init__(self,nome, hp, ataque, defesa, xp,dano_ultimate, inventaio,nome_ataque):
        super().__init__(nome, hp, ataque, defesa, xp,dano_ultimate, inventaio)
        self.nome_ataque = nome_ataque
    
    def atacar(self, oponente):
        super().atacar(oponente)
        print(f'{self._nome} avança e {self.nome_ataque}, deferindo \033[31m{self._ataque}\033[0m de dano')
    

#--MOB_ELITE                NOME           |HP||ATK|DEF||XP|
orc            = MobElite('Orc',           380, 80, 60, 20 , 100, [], 'ataca com fúria selvagem!')
troll          = MobElite('Troll',         550, 70, 95, 25, 80, [], 'ergue seu enorme braço e ataca com violência!')
vampiro        = MobElite('Vampiro',       420, 75, 55, 22, 90, [], 'desfere um golpe envolto em trevas!')
gargula        = MobElite('Gargula',       340, 90, 70, 20, 120, [], 'desfere um golpe com suas garras de pedra !')
golem_de_pedra = MobElite('Golem de Pedra',650, 65,160, 28, 60, [], 'tenta esmagá-lo contra o chão!')


lista_mob_elite = [orc,troll,vampiro,gargula,golem_de_pedra]

