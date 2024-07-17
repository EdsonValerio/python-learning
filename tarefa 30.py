velo = float(input('Qual é a velocidade atual do carro? '))
if velo > 80:
    print('Multado')
    multa =  (velo-80) * 7
    print('Você deve pagar uma multa de {:.2f}'.format(multa))
else:
    print('Você esta dentro do limite de velocidade! Boa viagem! ')
