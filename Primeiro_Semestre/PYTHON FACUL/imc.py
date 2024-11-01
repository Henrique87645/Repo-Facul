peso = float(input("Esvreva o seu peso em kg: "))
altura = float(input("Escreva sua altura em metros: "))
imc = peso / (altura**2)
if (imc <= 18.5):
    print("Abaixo do peso")
elif (imc > 18.5) == (imc <24.9):
    print ("Peso normal")
elif (imc > 25) == (imc < 29.5):
    print("sobrepeso")
else:
    (imc > 30)
    print("Você é obeso")