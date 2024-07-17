print('==' * 8, 'LOJAS EDSIN', '==' * 8 )
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
    [ 1 ] à vista dinheiro/cheque 
    [ 2 ] à vista cartão
    [ 3 ] 2x no cartão 
    [ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção de pagamento? '))
if opção == 1:
    preço1 = preço - (preço * 10 / 100)
    print('Sua compra de R${:.2f}, vai custar R${:.2f}.'.format(preço, preço1))
elif opção == 2:
    preço2 = preço - (preço * 5 / 100)
    print('Sua compra de R${:.2f}, vai custar R${:.2f}'.format(preço, preço2))
elif opção == 3:
    preço3 = preço
    parcela = preço3 / 2
    print('Sua compra de R${:.2f} será parcelada em 2x de {:.2f} SEM JUROS.'.format(preço, parcela))
elif opção == 4:
    x = int(input('Digite a quantidade de parcelas: '))
    preço4 = preço + (preço * 20 / 100)
    parcela =  preço4 / x
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(x, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, preço4))
else:
    print('Opção invalida, digite novamente')
