#Números primos
#
#i=inicio
#f=fim
#n=numero
#p=primo

i = 1
f = int(input("Digite até qual número quer saber se é primo: "))

for n in range(i, f + 1):
    if n > 1:
        p = True 
        for i in range(2, int(n * 0.5) + 1):
            if (n % i) == 0:
                p = False 
                break
        if p: 
            print(str(n) + " É primo. ")