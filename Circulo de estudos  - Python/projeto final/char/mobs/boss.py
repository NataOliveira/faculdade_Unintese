from char.base_char import BaseChar

class Boss(BaseChar):

    def __init__(self,nome, hp, ataque, defesa, xp, dano_ultimate, inventario):
        super().__init__(nome,hp, ataque, defesa, xp, dano_ultimate, inventario)
           

    
        

# -BOSS-                     NOME                   |HP||ATK|DEF||XP||ESPECIAL|
rei_goblin          = Boss('Rei Goblin',           1500, 180, 80, 500,  220, [])
senhor_dos_zumbis   = Boss('Senhor dos Zumbis',    1800, 160, 65, 550,  180, [])
cavaleiro_esqueleto = Boss('Cavaleiro Esqueleto',  1700, 210, 95, 580,  260, [])
alfa_das_trevas     = Boss('Alfa das Trevas',      2000, 250, 75, 650,  310, [])

lista_bosses = [rei_goblin,senhor_dos_zumbis,cavaleiro_esqueleto,alfa_das_trevas]