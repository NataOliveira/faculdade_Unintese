'''
Personagem de RPG
Nome 
CLasse
HP
'''

'Nome da Classe'
class Personagem:

    lista_personagens = []

    'Atributos'
    def __init__(self,nome,classe,hp):
        self.nome = nome
        self.classe = classe
        self.hp = hp
        Personagem.lista_personagens.append(self)

    'metodos => funçao => def'
    def gritar(self):
        print(f' {self.nome} : AAAAAAHh')

    def apresentar_personagens():
        for i in Personagem.lista_personagens:
            print(i.nome)
        

'Criar um objeto => Instanciar um Objeto'
vilao = Personagem('Medesa','mage', 24000)
heroi = Personagem('Keliton','warrior', 1200)


Personagem.apresentar_personagens()