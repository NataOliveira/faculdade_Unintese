from char import *
from random import randint
from time import sleep
import msvcrt

personagem = []


while True:
    
    print('''
    Bem-vindo ao jogo! Selecione o caminho que você vai trilhar:

    ⚔️ Soldado       Selecione ==> 1
    🔮 Mago         Selecione ==> 2
    🏹 Atirador     Selecione ==> 3

    ''')

    try:
        opcao = int(msvcrt.getch())
        
        match opcao:
            case 1:
                while True:

                    print('Soldado Selecionado, escolhar qual heróivocê quer invocar para o campo de batalha:')
                    print(f'\n{aquiles.nome}     | Ataque: {aquiles.ataque}     |Defesa: {aquiles.defesa}   |Poder Especial: {aquiles.ataque_especial}   Selecione ==> 1')
                    print(f'\n{joana_darc.nome} | Ataque: {joana_darc.ataque}     |Defesa: {joana_darc.defesa}   |Poder Especial: {joana_darc.ataque_especial}   Selecione ==> 2')
                    print(f'\n{leonidas.nome}    | Ataque: {leonidas.ataque}     |Defesa: {leonidas.defesa}   |Poder Especial: {leonidas.ataque_especial}   Selecione ==> 3\n')

                    try:
                        soldado_escolhido = int(msvcrt.getch())
                        match soldado_escolhido:
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
                print('Soldado Selecionado')
                break
            case 3:
                print('Soldado Selecionado')
                break
            case _:
                print('Numero Inválido, selecione apenas 1, 2 ou 3')
                print('pressione qualquer tecla para voltar')
                msvcrt.getch()
       
    except ValueError:
        print('Numero inválido')

print(f'Herói selecionado: {personagem.nome}')