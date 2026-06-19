from random import randint 
import copy
from char import *
import msvcrt

def selecionar_heroi(heroi):  

       
    def printherois(classe, hero):

        print('\n'*20 + f'''\033[32mClasse\033[0m {classe} \033[32mSelecionada, escolher qual herói você quer invocar para o campo de batalha:\033[0m

        Herói     | HP    | Ataque   | Defesa  | Ultimate\n''')
    
        for indice, i in enumerate (hero):
            print(f'({indice+1}) \033[4m {i.nome:<12} | {i.hp:<5} | {i.ataque:<8} | {i.defesa:<7} | {i.dano_ultimate} \033[0m')
        
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
        
            {personagem.nome}
        HP     :     {personagem.hp}
        Ataque :     {personagem.ataque}
        Defesa :     {personagem.defesa}
        Ultimate:    {personagem.dano_ultimate}\n''')

    return personagem

def mob_fraco_spawner():

    mob_spawner = lista_mob_fraco[randint(0,3)]
    mob_spawner.inventario = mob_spawner.items()
    return copy.deepcopy(mob_spawner)

def mob_elite_spawner():

    mob_spawner = lista_mob_elite[randint(0,len(lista_mob_elite)-1)]
    mob_spawner.inventario = mob_spawner.items()
    return copy.deepcopy(mob_spawner)

def boss_spa():

    mob_spawner = lista_bosses[randint(0,len(lista_bosses)-1)]
    mob_spawner.inventario = mob_spawner.items()
    return copy.deepcopy(mob_spawner)