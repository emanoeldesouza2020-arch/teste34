digite= int(input("digite quantos kilometros rodou com o carro: "))
dias= int(input("digite a quantidade de dias que ficou o com o carro: "))
valor = (dias * 60) + (digite * 0.15)
print(f"o valor do aluguel do carro é de r$ {valor:.2f}")