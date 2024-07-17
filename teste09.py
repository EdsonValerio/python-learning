nome = str(input('Qual é o seu nome? '))
if nome == 'Edson':
    print('Que lindo nome!')
elif nome == 'Pedro'or nome == 'maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia {}'.format(nome))
