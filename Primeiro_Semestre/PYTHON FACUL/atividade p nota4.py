idade = int(input('Digite sua idade: '))
civil = input('Seu estado civil, S para solteiro, C para casado, V para viúvo e D para divorciado:')

if idade <= 30 and civil == 'S':
    print("Ainda está curtindo a vida!")

if civil == 'C':
    print("Desejamos felicidades ao casal!")

if civil == 'V':
    print("Meus pesames a sua perda")

if civil == 'D':
    print("A vida ainda não acabou, você vai achar o amor!")