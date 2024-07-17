from datetime import date
print('ALISTAMENTO MILITAR')
anoNasc = int(input('Ano de nascimento: '))
ano = date.today().year
anoAlis = (anoNasc + 18)
idade = (ano - anoNasc)
print('Quem nasceu em {}, tem {} anos em {}.'.format(anoNasc, idade, ano))
if idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}'.format(anoAlis))
elif idade == 18:
    print('Seu alistamento será em {}, aliste IMEDIATAMENTE!!'.format(anoAlis))
elif idade > 19:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento aconteceu em {}'.format(anoAlis))
