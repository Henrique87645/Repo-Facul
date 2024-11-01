sexo = str(input("Diga se seu sexo é F ou M: "))
altura = float(input("Digite sua altura: "))

if (sexo >= 'M') == (altura <= 1.80):
    print("Altura acima da média masculina")
else:
    print("Altura abaixo da média")

if (sexo >= 'F') == (altura <= 1.60):
    print("Altura abaixo da média feminina")

else:
    print("Altura acima da média")