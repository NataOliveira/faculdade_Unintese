

clientes = [
    {"nome": "Celso", "salario": 5.0, "garantia": "Sim", "nome_sujo": "Não"},
    {"nome": "Ana", "salario": 2.0, "garantia": "Sim", "nome_sujo": "Não"},
    {"nome": "Bruno", "salario": 1.0, "garantia": "Não", "nome_sujo": "Sim"},
    {"nome": "Maria", "salario": 4.0, "garantia": "Não", "nome_sujo": "Não"},
    {"nome": "Carlos", "salario": 2.5, "garantia": "Não", "nome_sujo": "Não"}
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