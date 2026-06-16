from item_cardapio import itemcardapio

class Prato(itemcardapio):
    def __init__(self,nome,preco,descricao):
       super().__init__(nome, preco)
       self.descricao = descricao

    def __str__(self):
        return self.descricao


f = Prato('Frango','12','frango com batata')

