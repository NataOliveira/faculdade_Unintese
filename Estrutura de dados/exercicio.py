from collections import deque
import time

lista_de_concluidos = []
fila = deque()

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
        
        lista_de_concluidos.append(chamado)

    def proximo_chamado():

        if fila:
         
         proximo_chamado = fila.popleft()
         return proximo_chamado
        
        else:
            return None
        
    def chamado_anterior():

        return lista_de_concluidos.pop

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

while len(fila) >= 1:


    opc = int(input("""
    1 - Próximo chamado
    2 - Finalizar Chamado
    3 - Consultar Ultimo Chamado \n"""))


    match opc:
    
        case 1:

            chamado_em_atendimento = Atendimento.proximo_chamado()

            if chamado_em_atendimento == None:
                continue
            else: 
                print(f"""
Nome:{chamado_em_atendimento.nome}
Descrição do Problema: {chamado_em_atendimento.problema}""")
        case 2:
            if chamado_em_atendimento == None:
                print('Nenhum chamando sendo atendido no momento')
                continue
            else:
                Atendimento.finalizar_chamado(chamado_em_atendimento)
                print("Chamado finalizado")
                

        case 3:

            chamado_em_atendimento = Atendimento.chamado_anterior()
            
            print(f"""
Nome:{chamado_em_atendimento.nome}
Descrição do Problema: {chamado_em_atendimento.problema}""")




