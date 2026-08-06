class Node:
    def __init__(self, dado): #caracteristicas
        self.dado = dado
        self.proximo = None #Nada
        


class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None

    def inserir_no_inicio(self, dado):
        novo_node = Node(dado)

        #passa para o lado o node que já existe
        novo_node.proximo = self.head

        #A cabeça da lista ela é atualizada para o novo node
        self.head = novo_node

        print(f'[{dado}] Inserido no Início')

    def exibier_lista(self):

        atual = self.head
        elementos = []

        while atual is not None:
            elementos.append(atual.dado)
            atual = atual.proximo
        print(elementos)

    def inserir_no_final(self):



lista = ListaEncadeada()

lista.inserir_no_inicio(1)
lista.inserir_no_inicio(2)
lista.inserir_no_inicio(3)
lista.exibier_lista()
