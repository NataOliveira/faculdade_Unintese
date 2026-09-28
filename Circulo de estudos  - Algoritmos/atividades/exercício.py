clientes = [
    {"nome": "Celso", "salario": 5.0, "garantia": "Sim", "nome_sujo": "Não"}, #0
    {"nome": "Ana", "salario": 2.0, "garantia": "Sim", "nome_sujo": "Não"},  #1
    {"nome": "Bruno", "salario": 1.0, "garantia": "Não", "nome_sujo": "Sim"}, #2
    {"nome": "Maria", "salario": 4.0, "garantia": "Não", "nome_sujo": "Não"}, #3
    {"nome": "Carlos", "salario": 2.5, "garantia": "Não", "nome_sujo": "Não"} #4
]


# Variáveis de Controle
aprovados = 0
analise_gerente = 0
reprovados = 0



print("--- Processando Lote de Empréstimos ---")


# O Loop Principal (Processamento em Lote)
for cliente in clientes:
    print(f"\nAnalisando cliente: {cliente['nome']}")
   
    # Lógica de Empréstimo (O emaranhado de IFs)
    if cliente['salario'] >= 3:
        if cliente['nome_sujo'] != 'Sim':
            print("Status: Crédito Aprovado")
            aprovados += 1
            

        else:
            if cliente['garantia'] == 'Sim':
                print("Status: Crédito Aprovado")
                aprovados += 1
            else:
                print("Status: Crédito Reprovado")
                reprovados += 1
    else:
        if cliente['garantia'] == 'Sim':
            print("Status: Passar por analise do gerente")
            analise_gerente += 1
        else:
            print("Status: Crédito Reprovado")
            reprovados += 1


print("\n--- Relatório Final ---")
print(f"Total Aprovados: {aprovados}")
print(f"Total Análise: {analise_gerente}")
print(f"Total Reprovados: {reprovados}")



# #escolhas

# if escolha == '1':
#     print('Bom dia')

# elif escolha == '2':
#     print('Bom tarde')
    
# elif escolha == '3':
#     print('Boa noite')

# else:
#     print('Você escolheu uma opção que não existe') 