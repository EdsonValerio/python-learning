from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for c in range (1, 8):
    n = int(input('Em que ano a {}° pessoa nasceu?? '.format(c)))
    idade = ano - n
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo temos {totmaior} pessoas maiores de idade')
print(f'E temos um total de {totmenor} pessoas menores de idade')