numero1 = int(input('Digite a numero 1:'))
numero2 = int(input('Digete a numero 2:'))
numero3 = int(input('Digite a numero 3:'))

x = numero1
y = numero2
z = numero3
maior = x

if y > maior:
    maior = y
if z > maior:
    maior = z
print(maior)
