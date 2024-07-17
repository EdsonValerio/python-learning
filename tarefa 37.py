numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal 
[ 3 ] Converter para Hexadecimal ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} Convertido para Binário é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} Convertido para Octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('{} Convertido para Hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida!')


