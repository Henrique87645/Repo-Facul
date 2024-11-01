sa = float(input("Digite seu salário e farei a conta: R$ "))
porcentagem = (sa * 0.1)
porcentagem1 = (sa * 0.05)
if sa < 1.500:
    print("Seu salarario com o acrecimo de 10% fica: R$ ", sa + porcentagem )

else:
    print("Seu salarario com o acrecimo de 5% fica: R$ ", sa + porcentagem1 )
