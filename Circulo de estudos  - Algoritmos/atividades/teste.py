import time

tamanho = 100000
lista = []
dicionario = {}

for i in range (tamanho):
    lista.append(i)
    dicionario[i] = True
    
    
print(f' ----- Testando com {tamanho} elementos ----- ')


print('Iniciando O(1) - Busca no Dicionário...')
inicio = time.time()

9999 in dicionario

fim = time.time()
tempo_o1 = fim - inicio
print(f' Tempo O(1): {tempo_o1:.10f} segundos')


print('Iniciando O(n) - Busca Simples na Lista...')
inicio = time.time()
9999 in lista
fim = time.time()
tempo_on = fim - inicio
print(f'Tempo O(n): {tempo_on:.10f} segundos')


print('Iniciando O(n²) - Comparação de todos com todos...')
inicio = time.time()
contagem = 0
amostra_n2 = 100000
for i in range(amostra_n2):
    for j in range (amostra_n2):
        contagem += 1

fim = time.time()
tempo_on2 = fim - inicio
print(f'Tempo O(n²): {tempo_on2:.10f} segundos leo o total de {amostra_n2}')
print("\n-------------------------------------------")
print("CONCLUSÃO PARA A TURMA:")
print(f"O(1)  é como achar uma página pelo índice.")
print(f"O(n)  é como ler o livro página por página.")
print(f"O(n²) é como ler o livro todo de novo a cada página lida!")