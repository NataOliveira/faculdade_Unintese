from char import *
from random import randint

import msvcrt
from functions import *

# SELECÃO DE HERÓI
personagem_select = None
hero = (selecionar_heroi(personagem_select))

print('\npressione qualquer tecla para começar a jornada !\n\n')
msvcrt.getch()


# 1 Laço game
game_over = False

#------Game até 100 XP| Mobs fracos-----
while hero._xp < 100 and not game_over:

    spawner = mob_fraco_spawner()
    hero, game_over = batalha(hero,game_over, spawner)


#------Batalha com Boss---------
while hero._xp < 100 and not game_over:

    spawner = boss_spawner()
    hero, game_over = batalha(hero,game_over, spawner)

#-----Mensagem de LEVEL UP---------
levelup(hero)


#------Game até 200 XP| Mobs fracos-----
while hero._xp < 200 and not game_over:

    spawner = mob_elite_spawner()
    hero, game_over = batalha(hero,game_over,spawner)


#------Batalha com Boss---------
while hero._xp < 100 and not game_over:

    spawner = boss_spawner()
    hero, game_over = batalha(hero,game_over, spawner)
        
if game_over:
    print('\n\n\n\n\033[31m-----Game Over-----\033[0m')
    print('Você foi derrotado')
    print(f'Seu Xp Final: {hero._xp}\n\n')

    
    
    
    

    