from char import *
from random import randint
from time import sleep
import msvcrt
from functions import *

# SELECÃO DE HERÓI
personagem_select = None
hero = (selecionar_heroi(personagem_select))

print('\npressione qualquer tecla para começar a jornada !\n\n')
msvcrt.getch()




# 1 Laço game
game_over = False

while hero.xp <= 1000 and not game_over:

    spawner = mob_fraco_spawner()
    print('\n' * 20 + f'''Um \033[31m{spawner.nome}\033[0m, foi invocado!!''')

    while spawner.hp > 0 and not game_over:

        print(f'''\n{spawner.nome} | HP: {spawner.hp}\n\n\n
-------------------------------
Seu HP: {hero.hp} | Seu XP Atual: {hero.xp}
\n1 - Atacar | 2 - Curar\n''')

        acao = int(msvcrt.getch())

        match acao:
            case 1:
                print('\n' * 20)
                BaseChar.atacar(hero)
                spawner.hp = spawner.hp - hero.ataque
                BaseChar.atacar(spawner)
                hero.hp = hero.hp - spawner.ataque
                if spawner.hp <= 0:
                    print(f'\n{spawner.nome} foi derrotado ! {spawner.inventario[0]['nome_item']}, foi dropado' + '\n' * 5 +
                          'Pressione qualquer tecla para próxima batalha...' + '\n' * 3)
                    
                    hero.inventario += spawner.inventario
                    hero.xp += spawner.xp
                    msvcrt.getch()

            case 2:
                print('\n' * 20)
                hero.hp = hero.hp + 100
                print(f'''Você Consumiu porção de cura !''')

            case _:
                print('\033[31mNumero Inválido, selecione apenas 1, 2 ou 3\033[0m')
                print('pressione qualquer tecla para voltar')
                msvcrt.getch()

            
        if hero.hp <= 0:
            game_over = True

if game_over:
    print('\nGame Over')
    print('Você foi derrotado')
    print(f'Seu XP Atual Final: {hero.xp}')

    

    
    

    