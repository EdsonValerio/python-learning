nome = str(input('Digite seu nome completo:')).strip()
nomeMA = nome.upper()
nomeMI = nome.lower()
quant = len(nome) - nome.count(' ')
prNome= nome.split(' ')
quantPrNome = nome.find(' ')
print('Analisando seu nome...')
print('Seu nome em maisuculas fica:' , nomeMA)
print('Seu nome me minusculas fica: ', nomeMI)
print('O seu nome, possui um total de', quant, 'caracteres.')
print('Seu primeiro nome:',prNome[0], ', e ele tem', quantPrNome, 'letras')