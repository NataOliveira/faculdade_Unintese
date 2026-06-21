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


while hero._xp <= 100 and not game_over:

    spawner = mob_fraco_spawner()
    print('\n' * 20 + f'''Um \033[31m{spawner._nome}\033[0m, foi invocado!!''')

    while spawner._hp > 0 and not game_over:

        print(f'''\n{spawner._nome} | HP: {spawner._hp}\n\n\n
-------------------------------
Seu HP: {hero._hp} | Seu XP Atual: {hero._xp}
\n1 - Atacar | 2 - Abrir inventário\n''')

        acao = int(msvcrt.getch())

        match acao:
            case 1:
               
               BaseChar.batalha(hero,spawner) 

            case 2:
                
                BaseChar.abrir_inventario(hero)
                msvcrt.getch()


            case _:
                print('\033[31mNumero Inválido, selecione apenas 1, 2 ou 3\033[0m')
                print('pressione qualquer tecla para voltar')
                msvcrt.getch()

            
        if hero._hp <= 0:
            game_over = True

levelup(hero)


while hero._xp <= 200 and not game_over:

    spawner = mob_elite_spawner()
    print('\n' * 20 + f'''Um \033[31m{spawner._nome}\033[0m, foi invocado!!''')

    while spawner._hp > 0 and not game_over:

        print(f'''\n{spawner._nome} | HP: {spawner._hp}\n\n\n
-------------------------------
Seu HP: {hero._hp} | Seu XP Atual: {hero._xp}
\n1 - Atacar | 2 - Abrir inventário\n''')

        acao = int(msvcrt.getch())

        match acao:
            case 1:
               
               BaseChar.batalha(hero,spawner) 

            case 2:
                
                BaseChar.abrir_inventario(hero)
                msvcrt.getch()


            case _:
                print('\033[31mNumero Inválido, selecione apenas 1, 2 ou 3\033[0m')
                print('pressione qualquer tecla para voltar')
                msvcrt.getch()

            
        if hero._hp <= 0:
            game_over = True


if game_over:
    print('\nGame Over')
    print('Você foi derrotado')
    print(f'Seu XP Atual Final: {hero._xp}')

    
    
    
    

    