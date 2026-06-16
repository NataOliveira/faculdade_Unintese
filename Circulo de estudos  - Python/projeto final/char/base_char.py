class BaseChar():

    def __init__(self,nome,hp,ataque,defesa,xp):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa
        self.xp = xp
        

    def atacar(self):
        print('Atacando')
        print(f'Dano: {self.ataque}')

   
            


    

