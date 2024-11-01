lado1 = float(input("Qual a medida do lado: "))
lado2 = float(input("Qual a medida do lado: "))
lado3 = float(input("Qual a medida do lado: "))
if (lado1 == lado2 == lado3):
    print("Ele é equilátero")
elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print("É isósceles")
else:
    print("É escaleno")