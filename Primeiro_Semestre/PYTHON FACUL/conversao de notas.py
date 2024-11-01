num = int(input("Digite um número d 0 a 100: "))

if (num >=90):
    print("Nota azul: A",num)
elif (num >= 80) == (num <= 89):
    print("Nota azul: B",num)
elif (num >= 70) == (num <= 79):
    print("nota azul rasa: C",num)
elif (num >= 60) == (num <= 69):
    print("Nota vermelha: D",num)
else:
    print("Nota baixa: F",num)
