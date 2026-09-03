class TabelaHash():
    def __init__(self,tamanho=8):
        self.tamanho = tamanho
        self.baldes = [[] for i in range (tamanho)]

    def _hash(self, chave):
        return sum( ord(c) for c in str(chave)) % self.tamanho

    def inserir(self,chave,valor):
        indice = self._hash(chave)
        for par in self.baldes[indice]:
            if par[0] == chave:
                par[1] = valor
                return
        self.baldes[indice].append([chave, valor])

    def buscar(self,chave):

        indice = self._hash(chave)
        for par in self.baldes[indice]:
            if par[0] == chave:
                return print(par[1])


catalogo = TabelaHash()

catalogo.inserir('morador 1','apt.404',)
catalogo.inserir('morador 2','apt.202')
catalogo.inserir('morador 3','apt.204')
catalogo.inserir('morador 4','apt.504',)
catalogo.inserir('morador 5','apt.203')
catalogo.inserir('morador 6','apt.604')

catalogo.buscar('morador 6')