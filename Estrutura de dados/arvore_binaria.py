class NoArvore:
    def __init__(self, valor):
        self.valor = valor 
        self.esquerda = None 
        self.direita = None
    

class ArvoreBuscar:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = NoArvore(valor)
        else:
            self._inserir(self.raiz, valor)
            
    def _inserir(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = NoArvore(valor)
            else:
                self._inserir(no.esquerda, valor)   
                
        else:
            if no.direita is None:
                no.direita = NoArvore(valor)
            else:
                self._inserir(no.direita, valor)
    
    def em_ordem(self, no):           #                      50
        if no:                        #                30         70
            self.em_ordem(no.esquerda)#            20       40
            print(no.valor)
            self.em_ordem(no.direita)
    
    def pre_ordem(self, no):
         if no:    
            print(no.valor)                    #                30         70
            self.pre_ordem(no.esquerda)#            20       40
            self.pre_ordem(no.direita)
    
    def pos_ordem(self, no):
         if no:                        #                30         70
            self.pos_ordem(no.esquerda)#            20       40
            self.pos_ordem(no.direita)
            print(no.valor)

arvore = ArvoreBuscar()

lista = [80,60,30,20,50]
for valor in lista:
    arvore.inserir(valor)

print("Printar em ordem")
arvore.em_ordem(arvore.raiz)
print("Printar em pré ordem")
arvore.pre_ordem(arvore.raiz)
print("Printar em pós ordem")
arvore.pos_ordem(arvore.raiz)