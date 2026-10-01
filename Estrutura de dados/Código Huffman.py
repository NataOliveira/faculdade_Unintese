"""
Compactação Huffman — aula extra (hoje).
Texto de teste: BANANA A aparece 3 vezes, N 2, B 1.
 Códigos: A=0, B=10, N=11
 Bits: 100110110 (9 bits em vez de 48 do ASCII)
"""
from pathlib import Path

class No:
    """
    Representa um nó na árvore de Huffman.
    Pode ser um nó folha (contendo um símbolo/caractere) ou um nó interno (agrupamento).
    """
    def __init__(self, freq, simbolo=None, esquerda=None, direita=None, ordem=0):
        self.freq = freq            # Frequência do símbolo ou a soma das frequências dos filhos
        self.simbolo = simbolo      # O caractere (apenas para nós folha)
        self.esquerda = esquerda    # Filho à esquerda na árvore
        self.direita = direita      # Filho à direita na árvore
        self.ordem = ordem          # Critério de desempate para a ordenação dos nós

    def eh_folha(self):
        """Verifica se o nó é uma folha (ou seja, possui um símbolo associado)."""
        return self.simbolo is not None

def contar(texto):
    """
    Calcula a frequência de cada caractere no texto fornecido.
    Retorna um dicionário onde a chave é o caractere e o valor é a sua contagem.
    """
    freq = {}
    for letra in texto:
        freq[letra] = freq.get(letra, 0) + 1
    return freq

def construir_arvore(freq):
    """
    Constrói a árvore de Huffman combinando os nós com as menores frequências.
    Retorna o nó raiz da árvore resultante.
    """
    floresta = []
    ordem = 0
    
    # Cria um nó folha para cada símbolo e adiciona à floresta (lista de nós)
    for simbolo in sorted(freq):
        floresta.append(No(freq[simbolo], simbolo, ordem=ordem))
        ordem += 1
        
    # Tratamento para o caso de um texto com apenas um tipo de caractere (ex: "AAAA")
    if len(floresta) == 1:
        unico = floresta[0]
        return No(unico.freq, esquerda=unico, ordem=ordem)
        
    # Combina os nós até que reste apenas um na floresta (a raiz da árvore)
    while len(floresta) > 1:
        # Ordena a floresta prioritariamente pela frequência e, em seguida, pela ordem de criação
        floresta.sort(key=lambda no: (no.freq, no.ordem))
        
        # Remove os dois nós com as menores frequências
        a = floresta.pop(0)
        b = floresta.pop(0)
        
        # Cria um novo nó pai combinando as frequências dos nós filhos
        pai = No(a.freq + b.freq, esquerda=a, direita=b, ordem=ordem)
        ordem += 1
        
        # Adiciona o novo nó pai de volta à floresta
        floresta.append(pai)
        
    return floresta[0]

def tabela_codigos(raiz):
    """
    Percorre a árvore de Huffman para gerar o código binário de cada símbolo.
    Retorna um dicionário mapeando os caracteres para as suas respectivas strings de bits.
    """
    codigos = {}
    
    def caminhar(no, prefixo):
        # Se for folha, associa o prefixo acumulado ao símbolo
        if no.eh_folha():
            # 'prefixo or "0"' garante que não retorne vazio caso a raiz seja o único nó
            codigos[no.simbolo] = prefixo or "0"
            return
        
        # ChamadFas recursivas: adiciona '0' ao ir para a esquerda e '1' ao ir para a direita
        caminhar(no.esquerda, prefixo + "0")
        caminhar(no.direita, prefixo + "1")
        
    caminhar(raiz, "")
    return codigos

def compactar(texto):
    """
    Executa o fluxo completo de compactação: contagem, criação da árvore,
    geração dos códigos e conversão do texto original em bits.
    """
    freq = contar(texto)                  # 1. Conta frequências
    raiz = construir_arvore(freq)         # 2. Constrói a árvore de Huffman
    codigos = tabela_codigos(raiz)        # 3. Gera a tabela de conversão
    
    # 4. Substitui cada letra do texto pelo seu código binário correspondente
    bits = "".join(codigos[letra] for letra in texto)
    
    return raiz, codigos, bits

def descompactar(raiz, bits):
    """
    Decodifica a string de bits de volta para texto utilizando a estrutura da árvore.
    """
    letras = []
    no = raiz
    
    # Percorre cada bit da string compactada
    for bit in bits:
        # Desce para a esquerda se o bit for "0", ou para a direita se for "1"
        no = no.esquerda if bit == "0" else no.direita
        
        # Ao alcançar um nó folha, o símbolo original foi encontrado
        if no.eh_folha():
            letras.append(no.simbolo)
            no = raiz # Reinicia a busca a partir da raiz para o próximo caractere
            
    return "".join(letras)

def salvar_huff(caminho, codigos, bits):
    """
    Salva o arquivo compactado em disco, armazenando a tabela de conversão e a string de bits.
    """
    with open(caminho, "w", encoding="utf-8") as arq:
        arq.write("HUFFMAN\n") # Cabeçalho de identificação do arquivo
        
        # Grava o dicionário de códigos
        for simbolo in sorted(codigos):
            arq.write(f"{simbolo} {codigos[simbolo]}\n")
            
        arq.write("---\n") # Separador entre os metadados e os dados comprimidos
        arq.write(bits)    # Grava a string de bits
        arq.write("\n")

def abrir_huff(caminho):
    """
    Lê o arquivo .huff do disco e extrai o dicionário de códigos e a string de bits.
    """
    with open(caminho, "r", encoding="utf-8") as arq:
        linhas = [linha.rstrip("\n") for linha in arq]
        
    # Validação simples do formato do arquivo
    if not linhas or linhas[0] != "HUFFMAN":
        raise ValueError("Arquivo .huff inválido.")
        
    codigos = {}
    i = 1
    
    # Lê a tabela de códigos até encontrar o separador '---'
    while i < len(linhas) and linhas[i] != "---":
        simbolo, codigo = linhas[i].split(" ", 1)
        codigos[simbolo] = codigo
        i += 1
        
    # O restante das linhas compõe a string de bits compactada
    bits = "".join(linhas[i + 1 :])
    return codigos, bits

def descompactar_tabela(codigos, bits):
    """
    Decodifica a string de bits de volta para o texto utilizando apenas o dicionário 
    (tabela de códigos), sem a necessidade da estrutura da árvore.
    """
    # Inverte o dicionário de {símbolo: código} para {código: símbolo}
    inverso = {codigo: simbolo for simbolo, codigo in codigos.items()}
    
    letras = []
    atual = ""
    
    for bit in bits:
        atual += bit # Acumula os bits progressivamente
        
        # Se a sequência atual corresponder a um código válido, traduz o caractere
        if atual in inverso:
            letras.append(inverso[atual])
            atual = "" # Reinicia o acumulador
            
    if atual:
        # Se sobrar algum bit não reconhecido no final, houve corrupção dos dados
        raise ValueError("Sobrou bit sem código. A tabela ou os bits estão errados.")
        
    return "".join(letras)

if __name__ == "__main__":
    # --- Bloco de Testes ---
    texto = "BANANA"
    raiz, codigos, bits = compactar(texto)
    
    print("Frequência:", contar(texto))
    print("Códigos:", codigos)
    print("Bits:", bits)
    
    # Exibe a diferença de tamanho (considerando 8 bits por caractere no padrão ASCII)
    print("Tamanho ASCII:", len(texto) * 8, "bits")
    print("Tamanho Huffman:", len(bits), "bits")
    
    # Teste de descompactação em memória
    volta = descompactar(raiz, bits)
    print("Volta pela árvore:", volta)
    
    # Teste de persistência e leitura no disco
    saida = Path(__file__).resolve().parent / "banana.huff"
    salvar_huff(saida, codigos, bits)
    
    tab, bits_arquivo = abrir_huff(saida)
    print("Volta pelo arquivo:", descompactar_tabela(tab, bits_arquivo))