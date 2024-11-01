preco = float(input("Insira o preço do produto: "))
desconto = preco * 0.1
comdesconto = preco - desconto

pag = int(input("forma de pagamento (1 para dinheiro, 2 para cartão): "))

if pag == 1:
    print(comdesconto)
else:
    print(preco)