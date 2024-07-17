from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
comp = randint(0, 2)
print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL 
      [ 2 ] TESOURA''')
jogador = int(input('Qual é a sua opção??'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 11)
print('O computador escolheu {}'.format(itens[comp]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=' * 11)
if comp == 0: 
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif comp == 1:
    if jogador == 0:
        print('COMPTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif comp == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
