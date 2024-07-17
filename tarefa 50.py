soma = 0
cont = 0
for c in range (1, 7):
    n = int(input('Digite o {}° valor:'.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
    else:
        print('Nenhum número PAR foi informado')
print('Você informou {} números pares, e a soma deles foi de {}'.format(cont, soma))
