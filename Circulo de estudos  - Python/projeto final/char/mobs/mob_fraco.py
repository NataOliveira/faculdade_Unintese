from char.base_char import BaseChar
from random import randint

class MobFraco(BaseChar):

    def __init__(self,nome, hp, ataque, defesa, xp,dano_ultimate, inventaio, nome_ataque):
        super().__init__(nome, hp, ataque, defesa, xp,dano_ultimate, inventaio)
        self.nome_ataque = nome_ataque
   
        
    def atacar(self, oponente):
        super().atacar(oponente)
        print(f'{self._nome} avança e {self.nome_ataque}, deferindo \033[31m{self._ataque}\033[0m de dano')
    
        
#--MOB_FRACO                NOME           |HP|           |ATK|DEF||XP|
goblin         = MobFraco('Goblin',        150,  randint(50,75), 20,  5, 0, [], 'chuta sua perna')
zumbi          = MobFraco('Zumbi',         180,  randint(50,75), 20,  8, 0, [], 'desfere um golpe podre!')
esqueleto      = MobFraco('Esqueleto',     140,  randint(50,75), 25,  7, 0, [], 'taca um osso')
lobo_selvagem  = MobFraco('Lobo Selvagem', 220,  randint(50,75), 15,  8, 0, [], 'Morde')

lista_mob_fraco = [goblin,zumbi,esqueleto,lobo_selvagem]

   