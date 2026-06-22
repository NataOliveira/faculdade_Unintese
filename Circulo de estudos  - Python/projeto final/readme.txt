

################################-Main-########################################


Arquivo main.py

Onde o jogo se inicia, chammando as funções do arquivo functions.py. Enquanto o jogador atender as condicionais o jogo continua.


#################################SuperClasse-BaseChar########################################

Arquivo char/base_char.py

SuperClasse BaseChar:

projetada para gerenciar atributos de personagens, inventários e funções de combate do jogo. a classe possui os atributos e métodos:


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

def atacar(self,oponente):

Aplica o dano de ataque básico diretamente no HP do oponente.Este método serve como base e será sobrescrito pelas subclasses através de polimorfismo

def ganhar_xp(self,oponente):

Faz o personagem receber o valor de Xp do oponente derrotado.

def ataque_ultimate(self):

fará o mesmo que o metodo atacar(). porém usando o dano_utlimate. (função em desenvolvimento)

def items(self):

Gera items de categoria (pequena, média ou grande) dos tipos de poção (cura, mana, fortalecimento ou defesa)

def abrir_inventario(self):

Agrupa, contabiliza e exibe no console os items dentro do inventário do personagem heroi.

def usar item(self):

Permitirá ao jogador escolher e consumir uma poção do inventário, aplicando uma melhoria nos atributos do personagem herói. (função em desonvolvimento)


def drop_items(self,hero):

Recebe uma poção aleatória da lista de items, adiciona no inventário do herói.



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


def levelup(): Mostra para o player que elevou o nível do jogo

def batalha(self, spawner):

Executa um ataque síncrono entre o herói e o oponente usando o valor do atributo ataque, mostrando no console o dano causado entre eles. E quando o oponente for derrotado o herói recebe o XP e item que o oponente possuía em seu inventário. 

