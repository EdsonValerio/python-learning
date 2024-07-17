import random
a1 =  input('primeiro aluno:')
a2 = input('segundo aluno')
a3 = input('terceiro aluno')
lista = [a1, a2, a3]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')


