
class restaurante():
    restaurantes = []
    def __init__(self,nome,cardapio):

        self.nome = nome
        self.cardapio = cardapio
        restaurante.restaurantes.append(self)

restaurante1 = restaurante('depressão','macarrao')
restaurante2 = restaurante('Fogao de lenha','churrasco')
