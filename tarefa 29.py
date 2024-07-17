import random
numeroy = int(input('Olá! Tente adivinhar qual o número de 1 a 5 o computador escolheu: '))
numeroX = random.randint(1, 5)
if numeroy == numeroX:
    print('Você acertou!! Meus parabens!!')
else:
    print('Errou!!')
print(f'O numero escolhido foi {numeroX}')
