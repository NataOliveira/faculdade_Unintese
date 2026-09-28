def analisar_credito(cliente):
    if cliente ['salario'] >= 3:
        if cliente ['nome_sujo'] != 'Sim':
            return 'Crédito Aprovado'
    elif cliente ['garantia'] == 'Sim':
            return 'Crédito Aprovado'   
    else:
        if cliente ['garantia'] == 'Sim':
            return 'Conversar com o Gerente'
        else :
             return 'Crédito Reprovado'
    
def processar_lote(lote):

    resultado = {'aprovados': 0, 'analise': 0, 'reprovados': 0}

    for pessoa in lote:
        status = analisar_credito(pessoa)

        if status == 'Crédito Aprovado':
            resultado ['aprovados'] += 1
        elif status == 'Conversar com o Gerente':
            resultado ['analise'] += 1
        else:
            resultado ['reprovados'] += 1

        print(f'Cliente: {pessoa ['nome']} | Status: {status}')
    return resultado    
        
def exibir_relatorio(dados):
    print("\n--- Relatório Final ---")
    print(f"Total Aprovados: {dados['aprovados']} ")
    print(f"Total Análise: {dados['analise']}")
    print(f"Total Reprovados:{dados['reprovados']}")


clientes = [
    {"nome": "Celso", "salario": 5.0, "garantia": "Sim", "nome_sujo": "Não"},
    {"nome": "Ana", "salario": 2.0, "garantia": "Sim", "nome_sujo": "Não"},
    {"nome": "Bruno", "salario": 1.0, "garantia": "Não", "nome_sujo": "Sim"},
    {"nome": "Maria", "salario": 4.0, "garantia": "Não", "nome_sujo": "Não"},
    {"nome": "Carlos", "salario": 2.5, "garantia": "Não", "nome_sujo": "Não"}
]


resultado = processar_lote(lote = clientes)



exibir_relatorio(dados = resultado)

