peso = float(input('Digite seu peso: (KG) '))
altura = float(input('Digite sua altura: (m) '))
imc =  peso / (altura ** 2)
print('Seu imc é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 18.5 and imc < 25: 
    print('Peso ideal!')
elif imc >= 25 and imc < 30:
    print('Sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Obesidade!!')
else:
    print('Obesidade Mórbida, gordo arrombado')