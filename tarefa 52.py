n = int(input('Digite um número: '))
tot = 0
for c  in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end = ' ')
        tot += 1
    else:
        print('\033[31m', end= ' ')
    print('{} '.format(c), end= ' ')
print('\n\033[m0 O número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('e por isso ele é PRIMO!')
else: 
    print('e por isso, ele NÃO É PRIMO')