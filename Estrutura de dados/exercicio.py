from collections import deque
import msvcrt
import time

lista_historico = []
fila = deque()
fila_n2 = deque()

class Chamado:
    def __init__(self,id,nome,problema):
        self.id = id
        self.nome = nome
        self.problema = problema

    def casdastrar_chamado(self):

        fila.append(self)
    
class Atendimento:
    def __init__(self,id):
        self.id = id
      
    def finalizar_chamado(chamado):
        
        lista_historico.append(chamado)

    def proximo_chamado():

        if fila:
         proximo_chamado = fila.popleft()
         return proximo_chamado
        
        else:
            return None

    def transferir_chamado(chamado):
    
        fila_n2.append(chamado)
            
    def consultar_chamado_anterior():
    
        return lista_historico[-1]
        
    def abrir_chamado_anterior():
        if lista_historico:
            return lista_historico.pop()
        
chamado1 = Chamado('1','Bruna','PC não liga')
fila.append(chamado1)
chamado2 = Chamado('2','Carlos','Teclado não funciona')
fila.append(chamado2)
chamado3 = Chamado('3','Ana','Mouse não funciona')
fila.append(chamado3)
chamado4 = Chamado('4','Pedro','Computador está muito lento')
fila.append(chamado4)
chamado5 = Chamado('5','Juliana','Monitor não apresenta imagem')
fila.append(chamado5)

chamado_em_atendimento = None
print("="*50)
logado = True
while logado:

    print("\n" * 20 + f""" 

Fila atual : {len(fila)} chamado(s) em espera
---------Disponível--------------

    1 - Próximo chamado
    2 - Consultar Ultimo Chamado
    3 - Sair do programa \n""")

    opc = int(msvcrt.getch()) 
    match opc:
        case 1:

            chamado_em_atendimento = Atendimento.proximo_chamado()

            if chamado_em_atendimento == None:
                print("\n" * 5 + "Nenhum chamado pendente")
            else: 
                print("\n" * 20 + f""" 
Nome:{chamado_em_atendimento.nome}
Descrição do Problema: {chamado_em_atendimento.problema}""")

            while opc == 1:
                print("""
---------Em Atendimento-------------
            
1 - Finalizar chamado
2 - Tansferir chamado
3 - Informações do chamado \n\n""")

                acao = int(msvcrt.getch())
                match acao:

                    case 1:
                        if chamado_em_atendimento == None:
                            print('Nenhum chamando sendo atendido no momento')
                            opc = 0
                            
                        else:
                            Atendimento.finalizar_chamado(chamado_em_atendimento)
                            print("Chamado finalizado")
                            chamado_em_atendimento = None
                            opc = 0

                    case 2:
                        print("Chamado Transferido")
                        Atendimento.transferir_chamado(chamado_em_atendimento)
                        chamado_em_atendimento = None
                        opc = 0

                    case 3:

                        if chamado_em_atendimento is None:
                            print("Nenhum chamado sendo atendido no momento")
                        else:
                            print("\n" * 20 + f"""
ID : {chamado_em_atendimento.id}
Nome:{chamado_em_atendimento.nome}
Descrição do Problema: {chamado_em_atendimento.problema}""")
                    
        case 2:

            if lista_historico:
                chamado_em_atendimento = Atendimento.consultar_chamado_anterior()
                print("\n" * 20 + f"""
Nome:{chamado_em_atendimento.nome}
Descrição do Problema: {chamado_em_atendimento.problema}

1 - Reabir chamado
2 - Voltar""")

                acao = int(msvcrt.getch())

                match acao:

                    case 1:
                        chamado_em_atendimento = Atendimento.abrir_chamado_anterior()
                        fila.appendleft(chamado_em_atendimento)
                    case 2:
                        pass
            else: 
                print("não há histórico de chamados")
                time.sleep(1)
        case 3:
            logado = False
            print("Atendimento encerrado")
        



