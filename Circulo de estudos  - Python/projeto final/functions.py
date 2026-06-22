from random import randint 
import copy
from char import *
import msvcrt

def selecionar_heroi(heroi):  

    def printherois(classe, hero):

        print('\n'*20 + f'''\033[32mClasse\033[0m {classe} \033[32mSelecionada, escolher qual herói você quer invocar para o campo de batalha:\033[0m

        Herói     | HP    | Ataque   | Defesa  | Ultimate\n''')
    
        for indice, i in enumerate (hero):
            print(f'({indice+1}) \033[4m {i._nome:<12} | {i._hp:<5} | {i._ataque:<8} | {i._defesa:<7} | {i._dano_ultimate} \033[0m')
        
        print ('\n'*5)

    while True:
    
        print('\n'*20 +'''\033[32mBem-vindo ao jogo! Selecione o caminho que você vai trilhar:\033[0m

        (1) - ⚔️  Soldado
        (2) - 🔮  Mago     
        (3) - 🏹  Atirador

        ''' + '\n'*5 )

        try:
            opcao = int(msvcrt.getch())
            
            match opcao:
                case 1:
                    while True:

                        print(lista_soldados)
                        printherois('⚔️  Soldado',lista_soldados)

                        try:
                            escolhido = int(msvcrt.getch())
                            match escolhido:
                                case 1:
                                    personagem = aquiles
                                    break
                                case 2:
                                    personagem = joana_darc
                                    break
                                case 3:
                                    personagem = leonidas
                                    break
                                case _:
                                    print('\033[31mNumero Inválido, selecione apenas 1, 2 ou 3\033[0m')
                                    print('pressione qualquer tecla para voltar')
                                    msvcrt.getch()
                        except ValueError:
                            print('\033[31misso não é um número\033[0m')
                    break
                                
                case 2:
                    while True:

                        printherois('🔮 Mago',lista_magos)
                        try:
                            escolhido = int(msvcrt.getch())
                            match escolhido:
                                case 1:
                                    personagem = merlin
                                    break
                                case 2:
                                    personagem = morgana
                                    break
                                case 3:
                                    personagem = gandalf
                                    break
                                case _:
                                    print('\033[31mNumero Inválido, selecione apenas 1, 2 ou 3\033[0m')
                                    print('pressione qualquer tecla para voltar')
                                    msvcrt.getch()
                        except ValueError:
                            print('\033[31misso não é um número\033[0m')
                    break    
                case 3:
                    while True:

                        printherois('🏹 Atirador',lista_atiradores)

                        try:
                            escolhido = int(msvcrt.getch())
                            match escolhido:
                                case 1:
                                    personagem = fallen
                                    break
                                case 2:
                                    personagem = garrus
                                    break
                                case 3:
                                    personagem = karl
                                    break
                                case _:
                                    print('\033[31mNumero Inválido, selecione apenas 1, 2 ou 3\033[0m')
                                    print('pressione qualquer tecla para voltar')
                                    msvcrt.getch()
                        except ValueError:
                            print('\033[31misso não é um número\033[0m')
                    break        
                   
        except ValueError as erro:
            print(erro)

    print(f'''\033[32mHerói selecionado\033[0m : 
        
            {personagem._nome}
        HP     :     {personagem._hp}
        Ataque :     {personagem._ataque}
        Defesa :     {personagem._defesa}
        Ultimate:    {personagem._dano_ultimate}\n''')

    return personagem

def mob_fraco_spawner():

    mob_spawner = lista_mob_fraco[randint(0,3)]
   
    return copy.deepcopy(mob_spawner)

def mob_elite_spawner():

    mob_spawner = lista_mob_elite[randint(0,len(lista_mob_elite)-1)]
  
    return copy.deepcopy(mob_spawner)

def boss_spawner():

    mob_spawner = lista_bosses[randint(0,len(lista_bosses)-1)]

    return copy.deepcopy(mob_spawner)

def levelup(self):
    if self._xp >= 100:
        print('\n'*20 + '''  
Você deixou para trás as terras dominadas por criaturas comuns.
A partir de agora, inimigos mais poderosos surgirão em seu caminho.

              
 ⚔️   Os Mob Elites despertaram!

Eles possuem mais vida, causam mais dano e carregam recompensas valiosas. 
Prepare seus equipamentos, aprimore suas habilidades e prove seu valor em batalhas cada vez mais desafiadoras.\n\n''')
        msvcrt.getch()

def batalha(hero,game_over,spawner):

    print('\n' * 20 + f'''Um \033[31m{spawner._nome}\033[0m, foi invocado!!''')

    while spawner._hp > 0 and not game_over:

        print(f'''\n{spawner._nome} | HP: {spawner._hp}\n\n\n
-------------------------------
Seu HP: {hero._hp} | Seu XP Atual: {hero._xp}
\n 1 - Atacar | 2 - Usar ultimate | 3 - Abrir inventário\n''')

        acao = int(msvcrt.getch())
        
        match acao:
            
            case 1:
               
                hero.atacar(spawner)

                if spawner._hp > 0:

                    spawner.atacar(hero)
                
                else:
            
                    BaseChar.drop_items(spawner,hero)
                    BaseChar.ganhar_xp(hero, spawner)
                    
                    print(f'\n{spawner._nome} foi derrotado ! {spawner._inventario[0]['nome_item']}, foi dropado' + '\n' * 5 +
                    'Pressione qualquer tecla para próxima batalha...' + '\n' * 3)
                    msvcrt.getch()
                    
            case 2:

                cooldown = 0
                if cooldown > 0:
                    print('Habilidade em cooldown')
                    cooldown -= 1
                    msvcrt.getch()
                    batalha(hero,game_over,spawner)
                else:
                    hero.ultimate(spawner)
                    cooldown = 3
                    
                    

            case 3:
                BaseChar.abrir_inventario(hero)
                msvcrt.getch()

            case _:
                print('\033[31mNumero Inválido, selecione apenas 1, 2 ou 3\033[0m')
                print('pressione qualquer tecla para voltar')
                msvcrt.getch()

        if hero._hp <= 0:
            game_over = True
            

    return hero,game_over
