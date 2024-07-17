valorcasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos você deseja pagar: '))
calc =  valorcasa / (anos * 12) 
min = salario  * 30 /100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorcasa, anos), end = '')
print(' o valor da prestação será de R${:.2f}'.format(calc))
if calc <= min:
    print('Emprestimo concedido')
else: 
    print('Empréstimo negado!!!!')
