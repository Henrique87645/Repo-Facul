var = int(input("Digite algum número e confira se ele é primo: "))
resto = var%2
print(resto)
if (var == 2):
    print("Seu número é primo:",var)
elif (resto >=1):
    print("Seu número é primo",var)
else:
    print("Seu número não é primo",resto)
