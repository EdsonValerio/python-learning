nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media =  (nota1 + nota2) / 2
if media >= 5 and media < 7:
    print('Sua média foi de {}, Voce está de recuperação!!'.format(media))
elif media > 7: 
    print('Sua média foi de {}, Você foi APROVADO!!!'.format(media))
else:
    print('Sua média foi de {}, Voce está REPROVADO!'.format(media))
