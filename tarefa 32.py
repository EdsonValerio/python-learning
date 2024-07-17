km = float(input('Digite a distância da sua viagem: '))
print('Você está prestes a começar uma viagem de {:.2f}Km.'.format(km))
preço = km * 0.50
if km >200:
    preço2 = km * 0.45
    print('O valor da sua corrida será de R${:.2f}'.format(preço2))
else:
    print('O valor da sua corrida será de R${:.2f}'.format(preço))