#Escreva um programa que calcule a soma dos primeiros N números, onde N é fornecido pelo usuário.
N = int(input('N de soma: '))
soma = 0
for i in range(N+1):
    soma = soma +  i
    print(soma)
