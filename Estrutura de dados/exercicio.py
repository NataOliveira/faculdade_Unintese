from collections import deque

lista_de_concluidos = []
fila = deque()

class Chamado:
    def __init__(self,id,nome,problema):
        self.id = id
        self.nome = nome
        self.problema = problema

    def adicionar_na_fila(self):

        fila.append(self)
    
class Atendimento:
    def __init__(self, chamado):
        self.chamado = chamado
      
    def adicionar_na_lista_de_concluidos(self):

        lista_de_concluidos.append(self)
                     
    def proxima_chamado(self):

        print(fila.popleft())
        
    def chamado_anterior(self):

        print(lista_de_concluidos[-1])


chamado1 = Chamado('1','Bruna','PC não liga')
chamado2 = Chamado('2','Carlos','Teclado não funciona')
chamado3 = Chamado('3','Ana','Mouse não funciona')
chamado4 = Chamado('4','Pedro','Computador está muito lento')
chamado5 = Chamado('5','Juliana','Monitor não apresenta imagem')
chamado6 = Chamado('6','Lucas','Internet não conecta')
chamado7 = Chamado('7','Mariana','Impressora não imprime')
chamado8 = Chamado('8','Rafael','Sistema apresenta erro ao iniciar')
chamado9 = Chamado('9','Camila','Computador está desligando sozinho')
chamado10 = Chamado('10','Felipe','Senha de acesso bloqueada')


