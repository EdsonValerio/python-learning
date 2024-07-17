primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
décimo = primeiro + (10 - 1) * razao
for c in range( primeiro, décimo + razao, razao):
    print('{} '.format(c), end= '> ' )
print('Acabou')