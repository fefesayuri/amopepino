#Conversão de temeperatura 
#
#
print("Opção 1 - Converter graus Celsius para Fahrenheit. ")
print("Opção 2 - Converter graus Celsius para Kelvin. ")
print("Opção 3 - Converter graus Fahrenheit para Kelvin. ")
print("Opção 4 - Converter Kelvin para graus Celsius. ")

opcao = int(input("Digite a opção escolhida: "))
valor = float(input("Qual o valor? "))
if opcao == 1:
    f = valor * 1.8 + 32
    print(f)
elif opcao == 2:
    k = valor + 273
    print(k)
elif opcao == 3:
    k = valor * 9/5 + 305
    print(k)
elif opcao == 4:
    c = valor - 273.15
    print(c)


