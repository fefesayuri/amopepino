#Qual rota?
#
# Rr = rota mais rápida
# Re = rota mais econômica 
# Mp = média ponderada
# r = n° de rotas
# te = tempo
# t = trechos 
# c = comprimento 
# vm = velocidade média

input (3)

r = (1)
input (t) # type: ignore



r = int(input("Digite o número de rotas: "))
ro = int(input("Quantas rotas: "))
n = 1 
l = list (range(n, ro + 1))

for qr in l:
    o = "Rota"

rg = [f"{o} {i}" for i in range(1, ro + 1)]
t = float(input("Quantos trechos: "))
c = float(input("Qual a distancia: "))
vm = float(input("Qual a velocidade media: "))
print(str(rg))