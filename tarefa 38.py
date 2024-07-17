print('Digite dois valores para saber qual o maior: ')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O número {}, é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O número {}, é maior que {}'.format(n2, n1))
else:
    print('Os números são iguais!!')
