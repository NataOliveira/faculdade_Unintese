from random import randint
import msvcrt

class BaseChar():

    def __init__(self, nome,hp,ataque,defesa,xp,dano_ultimate,inventario):
        self._nome = nome
        self._hp = hp
        self._ataque = ataque
        self._defesa = defesa
        self._xp = xp
        self._dano_ultimate = dano_ultimate
        self._inventario = inventario
        
    def atacar(self,oponente):
        oponente._hp -= self._ataque
        return self._ataque    
    
    def ganhar_xp(self,oponente):

        self._xp += oponente._xp
    
    def ultimate(self,oponente):
        oponente._hp -= self._dano_ultimate
        return self._dano_ultimate    

    def pocoes_lista():
      
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

        lista_pocoes = [porcoes_pequenas, porcoes_medias, porcoes_grandes]

        return lista_pocoes
        
    def drop_items(self,hero):

        lista_item_drop = BaseChar.pocoes_lista()
        lista_pocoes =  lista_item_drop[randint(0,len(lista_item_drop)-1)]
        uma_pocao_aleatoria = lista_pocoes[randint(0,len(lista_pocoes)-1)]

        self._inventario += uma_pocao_aleatoria
        hero._inventario += self._inventario
        
    def abrir_inventario(self):
        print('\n' * 5)
        print(f'''-------inventário-------\n
       Items             |quantidade|             
              ''')
        
        inventario_pocoes = {"vida": {"pequena": 0, "media": 0, "grande": 0},
                             "mana": {"pequena": 0, "media": 0, "grande": 0},
                            "defesa": {"pequena": 0, "media": 0, "grande": 0},
                            "fortalecimento": {"pequena": 0, "media": 0, "grande": 0},
} 

        for i in self._inventario:

            if i['nome_item'] == 'Porção de vida':
                inventario_pocoes['vida']['pequena'] +=1

            elif i['nome_item'] == 'Porção de mana':
                inventario_pocoes['mana']['pequena'] +=1

            elif i['nome_item'] == 'Poção de Fortalecimento':
                inventario_pocoes['fortalecimento']['pequena'] +=1

            elif i['nome_item'] == 'Porção de defesa':
                inventario_pocoes['defesa']['pequena'] +=1

            elif i['nome_item'] == 'Porção de vida média':
                inventario_pocoes['vida']['media'] +=1

            elif i['nome_item'] == 'Porção de mana média':
                inventario_pocoes['mana']['media'] +=1

            elif i['nome_item'] == 'Porção de fortalecimento média':
                inventario_pocoes['fortalecimento']['media'] +=1

            elif i['nome_item'] == 'Porção de defesa média':
                inventario_pocoes['defesa']['media'] +=1

            elif i['nome_item'] == 'Porção de vida grande':
                inventario_pocoes['vida']['grande'] +=1

            elif i['nome_item'] == 'Porção de mana grande':
                inventario_pocoes['mana']['grande'] +=1

            elif i['nome_item'] == 'Porção de fortalecimento grande':
                inventario_pocoes['fortalecimento']['grande'] +=1

            elif i['nome_item'] == 'Porção de defesa grande':
                inventario_pocoes['defesa']['grande'] +=1
  
# Procura quais items tem no iventario e mostra na tela
        if inventario_pocoes['vida']['pequena'] > 0:
            print(f"{'Porção Vida Pequena:':<30} {inventario_pocoes['vida']['pequena']}")

        if inventario_pocoes['vida']['media'] > 0:
            print(f"{'Porção Vida Média:':<30} {inventario_pocoes['vida']['media']}")

        if inventario_pocoes['vida']['grande'] > 0:
            print(f"{'Porção Vida Grande:':<30} {inventario_pocoes['vida']['grande']}")

        if inventario_pocoes['mana']['pequena'] > 0:
            print(f"{'Porção Mana Pequena:':<30} {inventario_pocoes['mana']['pequena']}")

        if inventario_pocoes['mana']['media'] > 0:
            print(f"{'Porção Mana Média:':<30} {inventario_pocoes['mana']['media']}")

        if inventario_pocoes['mana']['grande'] > 0:
            print(f"{'Porção Mana Grande:':<30} {inventario_pocoes['mana']['grande']}")

        if inventario_pocoes['fortalecimento']['pequena'] > 0:
            print(f"{'Porção Fortalecimento Pequena:':<30} {inventario_pocoes['fortalecimento']['pequena']}")

        if inventario_pocoes['fortalecimento']['media'] > 0:
            print(f"'{'Porção Fortalecimento Média:':<30} {inventario_pocoes['fortalecimento']['media']}")

        if inventario_pocoes['fortalecimento']['grande'] > 0:
            print(f"{'Porção Fortalecimento Grande:':<30} {inventario_pocoes['fortalecimento']['grande']}")

        if inventario_pocoes['defesa']['pequena'] > 0:
            print(f"{'Porção Defesa Pequena:':<30} {inventario_pocoes['defesa']['pequena']}")

        if inventario_pocoes['defesa']['media'] > 0:
            print(f"{'Porção Defesa Média:':<30} {inventario_pocoes['defesa']['media']}")

        if inventario_pocoes['defesa']['grande'] > 0:
            print(f"{'Porção Defesa Grande:':<30} {inventario_pocoes['defesa']['grande']}")
        print('\n' * 2)

    def usar_item(self):
        pass