from random import randint

class BaseChar():

    def __init__(self, nome,hp,ataque,defesa,xp,dano_ultimate,inventario):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa
        self.xp = xp
        self.dano_ultimate = dano_ultimate
        self.inventario = inventario
        
    def atacar(self):
        print(f'{self.nome} ataca, deferindo \033[31m{self.ataque}\033[0m de dano')
        
    def ultimate(self):
        print(f'{self.nome} ataca, deferindo \033[31m{self.ultimate}\033[0m de dano')

    def items(self):
      
        porcao_cura                     = [{'nome_item': 'Porção de vida', 'descricao': f'Um líquido vermelho brilhante que acelera a recuperação do corpo. Ao ser consumida, restaura 20% da vida do usuário.', 'quantidade': 0.20 }]
        porcao_mana                     = [{'nome_item': 'Porção de mana', 'descricao': f'Uma essência azul repleta de energia arcana. Reabastece as reservas mágicas e permite conjurar mais feitiços, restaura 15% da mana do usuário.', 'quantidade': 0.20 }]
        porcao_de_fortalecimento        = [{'nome_item': "Poção de Fortalecimento", 'descricao': "Um tônico raro preparado por alquimistas de batalha. Sua fórmula fortalece músculos e reflexos, aumentando o ataque do usuário em 20% durante o combate.",'quantidade': 0.20}]
        porcao_protecao                 = [{'nome_item': 'Porção de defesa', 'descricao': f'Uma mistura reforçada com minerais encantados que endurece a pele e fortalece em 30% a armadura contra ataques inimigos.', 'quantidade': 0.30 }]

        porcoes_pequenas = [porcao_cura,porcao_mana,porcao_de_fortalecimento,porcao_protecao]

        porcao_cura_media               = [{'nome_item': 'Porção de vida média', 'descricao': f'Um líquido vermelho brilhante que acelera a recuperação do corpo. Ao ser consumida, restaura 35% da vida do usuário.', 'quantidade': 0.35 }]
        porcao_mana_media               = [{'nome_item': 'Porção de mana média', 'descricao': f'Uma essência azul repleta de energia arcana. Reabastece as reservas mágicas e permite conjurar mais feitiços, restaura 30% da mana do usuário.', 'quantidade': 0.30 }]
        porcao_de_fortalecimento_media  = [{'nome_item': "Poção de Fortalecimento Média", 'descricao': "Um tônico raro preparado por alquimistas de batalha. Sua fórmula fortalece músculos e reflexos, aumentando o ataque do usuário em 40% durante o combate.",'quantidade': 0.40}]     
        porcao_protecao_media           = [{'nome_item': 'Porção de defesa média', 'descricao': f'Uma mistura reforçada com minerais encantados que endurece a pele e fortalece em 50% a armadura contra ataques inimigos.', 'quantidade': 0.50 }]

        porcoes_medias = [porcao_cura_media,porcao_mana_media,porcao_de_fortalecimento_media,porcao_protecao_media]

        porcao_cura_grande              = [{'nome_item': 'Porção de vida grande', 'descricao': f'Um líquido vermelho brilhante que acelera a recuperação do corpo. Ao ser consumida, restaura 60% da vida do usuário.', 'quantidade': 0.60 }]
        porcao_mana_grande              = [{'nome_item': 'Porção de mana grande', 'descricao': f'Uma essência azul repleta de energia arcana. Reabastece as reservas mágicas e permite conjurar mais feitiços, restaura 55% da mana do usuário.', 'quantidade': 0.55 }]
        porcao_de_fortalecimento_grande = [{'nome_item': "Poção de Fortalecimento", 'descricao': "Um tônico raro preparado por alquimistas de batalha. Sua fórmula fortalece músculos e reflexos, aumentando o ataque do usuário em 60% durante o combate.",'quantidade': 0.60}]        
        porcao_protecao_grande          = [{'nome_item': 'Porção de defesa grande', 'descricao': f'Uma mistura reforçada com minerais encantados que endurece a pele e fortalece em 70% a armadura contra ataques inimigos.', 'quantidade': 0.70 }]

        porcoes_grandes = [porcao_cura_grande,porcao_mana_grande,porcao_de_fortalecimento_grande,porcao_protecao_grande]

        lista_porcoes = [porcoes_pequenas, porcoes_medias, porcoes_grandes]

        x = lista_porcoes[randint(0,len(lista_porcoes)-1)]
        y = x[randint(0,len(x)-1)]

        self.inventario += y
        
        return y

    
        
# personagem = BaseChar ('Natan', 100,100,100,100,[],100)

# personagem.drop_item()


# print(personagem.inventario[0]['descricao'])
        
   
            


    

