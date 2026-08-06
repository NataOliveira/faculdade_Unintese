class Faixa:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None
        self.anterior = None


class ReprodutorApp:
    def __init__(self):
        self.faixa_atual = None

    def adicionar_na_fila(self, musica):
        nova_faixa = Faixa(musica)

        if self.faixa_atual is None:

            self.faixa_atual = nova_faixa
            print(f'Playlist Iniciada. Tocando: {self.faixa_atual.musica}')

        else:
            nova_faixa.anterior = self.faixa_atual
            nova_faixa.proximo = self.faixa_atual.proximo

            if self.faixa_atual.proximo:
                self.faixa_atual.proximo.anterior = nova_faixa

            self.faixa_atual.proximo = nova_faixa


    def proxima_faixa(self):
        if self.faixa_atual and self.faixa_atual.proximo:
            self.faixa_atual = self.faixa_atual.proximo
            print(f">>> Avançou para:  {self.faixa_atual.musica}")
        else:
            print("fim da playlist")

    def faixa_anterior(self):
            if self.faixa_atual and self.faixa_atual.anterior:
                self.faixa_atual = self.faixa_atual.anterior
                print(f"<<< Voltou para:  {self.faixa_atual.musica}")
            else:
                print("fim da playlist")


player = ReprodutorApp()

player.adicionar_na_fila("zuleide me ama")
player.adicionar_na_fila("tempo dos imbu")
player.adicionar_na_fila("nega do suvaco cabeludo")


print('''----ações do usuário----''')

player.proxima_faixa()
player.faixa_anterior()
player.proxima_faixa()
player.proxima_faixa()
player.faixa_anterior()
player.proxima_faixa()
player.faixa_anterior()
player.proxima_faixa()
player.proxima_faixa()
player.faixa_anterior()
player.faixa_anterior()
player.faixa_anterior()
player.faixa_anterior()
player.faixa_anterior()
player.faixa_anterior()
player.faixa_anterior()
