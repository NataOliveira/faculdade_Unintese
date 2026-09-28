n1 = 0
n2 = 1

numero = int(input("Numero: "))

for i in range (numero):
    vf = n1 + n2
    print (f'{i+1}º NUMERO = {vf}')
    n1 = n2 
    n2 = vf

