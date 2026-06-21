

################################-Main-########################################


Arquivo main.py

Onde o jogo se inicia, chammando as funções do arquivo functions.py e métodos da SuperClasse BaseChar. enquanto jogador atender as condicionais o jogo continua.


#################################SuperClasse-BaseChar########################################

Arquivo char/base_char.py

SuperClasse BaseChar:

projetada para gerenciar atributos de personagens, inventários e funções de combate num jogo de RPG. a classe possui os atributos e métodos:


Atributos:

Representa um personagem do jogo:

def __init__(self, nome,hp,ataque,defesa,xp,dano_ultimate,inventario):
self.nome (str) = O nome de identificação do personagem
self.hp	 (int) = Os pontos de vida atuais do personagem.
self.ataque (int) = O valor de dano base.
self.defesa (int) =  O valor de armadura para absorver danos recebidos.
self.xp (int) =  Os pontos de experiência acumulados pelo personagem.
self.dano_ultimate (int) = O valor de dano causado pela habilidade suprema.
self._inventário (lista) =  lista que armazena a lista de itens.


Métodos:

def atacar(self,spawner):

mostra no console o ataque do personagem, mostrando o dano causado.

def ataque_ultimate(self):

mostra no console o dano causado pela ultimate do personagem.

def items(self):

Gera e seleciona aleatoriamente uma categoria (Pequena, Média ou Grande) e um tipo de poção (Cura, Mana, Fortalecimento ou Defesa), inserindo-a no inventário e retornando o item ganho.

def abrir_inventario(self):

Agrupa, contabiliza e exibe no console os items dentro do inventário do personagem.

def usar item(self):

função retornará uma poção que o personagem tiver no inventário escolhida pelo jogador, aprimorando o status do personagem.

def batalha(sellf, spawner):

Executa um ataque síncrono entre o herói e o oponente usando o valor do atributo ataque, mostrando no console o dano causado entre eles. E quando o oponente for derrotado o herói recebe o XP e item que o oponente possuía em seu inventário. 



##############################SubClasse-Mobs#############################################
Arquivo char/mobs/mob_fraco.py

uma subclasse que herda os atributos e métodos da superclasse BaseChar importada de base_char.py, para instanciar os monstros do tipo mob_fraco.


Arquivo char/mobs/mob_elite.py

uma subclasse que herda os atributos e métodos da superclasse BaseChar importada de base_char.py, para instanciar os monstros do tipo mob_elite.


Arquivo char/mobs/boss.py

uma subclasse que herda os atributos e métodos da superclasse BaseChar importada de base_char.py, para instanciar os monstros do tipo Boss.


##############################SubClasse-Herois#############################################

Arquivo char/herois/atirador.py

uma subclasse que herda os atributos e métodos da superclasse BaseChar importada de base_char.py, para instanciar os herois do tipo atirador.


Arquivo char/herois/mago.py

uma subclasse que herda os atributos e métodos da superclasse BaseChar importada de base_char.py, para instanciar os herois do tipo mago.


Arquivo char/herois/soldado.py

uma subclasse que herda os atributos e métodos da superclasse BaseChar importada de base_char.py, para instanciar os herois do tipo soldado.





#################################Funções########################################

Arquivo functions.py

Arquivo para gerenciar laços de decisão do jogo

def selecionar heróis(herói):

função mostrará qual classe o jogador deseja jogar, e em seguida mostrará quais personagem aquela classe possui, mostrando também seus atributos(hp,ataque,defesa e ultimate). assim retornando o herói selecionado para arena.

def mob_fraco_spawner():

função gera e retorna uma cópia aleatória de um mob da classe mob_fraco.

def mob_elite_spawner():

função gera e retorna uma cópia aleatória de um mob da classe mob_elite.

def boss_spawner():

função gera e retorna uma cópia aleatória de um mob da classe boss.



