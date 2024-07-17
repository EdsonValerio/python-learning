from datetime import date
print('DEFINIÇÃO CATEGORIA NATAÇÃO')
anoAtual = date.today().year
anoNasc = int(input('Digite o ano de nascimento do atleta: '))
idade = anoAtual - anoNasc
print('O atleta nascido em {}, tem atualmente {} anos.'.format(anoNasc, idade))
if idade <= 9:
    print('O atleta tem {} anos, e será de categoria MIRIM (até 9 anos).'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos'.format(idade))
    print('e será da categoria INFANTIL (10 - 14 Anos).')
elif idade <= 19:
    print('O atleta tem {} anos, e será da categoria JÚNIOR (15 - 19 Anos).'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos, e será da categoria SÊNIOR (20 - 25 Anos)'.format(idade))
elif idade >= 25:
    print('O atleta tem {} anos, e será da categoria MASTER (25+ Anos).'.format(idade))
