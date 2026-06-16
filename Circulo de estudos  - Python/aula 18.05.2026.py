# lista = [30,20,10]
# media = sum(lista)/len(lista)
# print(f'A média da lista foi de {media}')



lista = [
    {'nome':'joao','idade':'12'},
    {'nome':'pedro','idade':'9'},
    {'nome':'caio','idade':'11'}
         ]


for i in lista:
    print (f'Nome: {i['nome']} | Idade: {i['idade']}')