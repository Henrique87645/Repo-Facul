N = int(input('N de Fibonatti: '))
soma = 0
for i in range(N+1):
    soma = soma +  i
#     1   =  1
#     1   =  0   +   1
#     3   =  1   +   2
#     6   =  3   +   3
#     10  =  6   +   4
#     15  =  10  +   5
    print(soma)