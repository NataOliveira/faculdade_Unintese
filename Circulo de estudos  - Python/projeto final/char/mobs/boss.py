from char.base_char import BaseChar
from random import randint

class Boss(BaseChar):

    def __init__(self,nome, hp, ataque, defesa, xp, dano_ultimate, inventario,nome_ataque):
        super().__init__(nome,hp, ataque, defesa, xp, dano_ultimate, inventario)
        self.nome_ataque = nome_ataque
    
    def atacar(self, oponente):
        super().atacar(oponente)
        print(f'{self._nome} avança e {self.nome_ataque}, deferindo \033[31m{self._ataque}\033[0m de dano')


# -BOSS-                     NOME                   |HP||ATK|DEF||XP||ESPECIAL|
rei_goblin          = Boss('Rei Goblin',           1500, 180, 80, 500,  220, [], 'libera a fúria de sua horda!')
senhor_dos_zumbis   = Boss('Senhor dos Zumbis',    1800, 160, 65, 550,  180, [], 'ergue os mortos do chão!')
cavaleiro_esqueleto = Boss('Cavaleiro Esqueleto',  1700, 210, 95, 580,  260, [], 'desfere um corte preciso com sua espada enferrujada!')
alfa_das_trevas     = Boss('Alfa das Trevas',      2000, 250, 75, 650,  310, [], 'rasga sua presa com garras sombrias!')

lista_bosses = [rei_goblin,senhor_dos_zumbis,cavaleiro_esqueleto,alfa_das_trevas]

